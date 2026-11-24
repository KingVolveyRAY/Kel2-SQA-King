"""
prompts_bank.py
Central repository of Prompt Engineering templates used across the experiments:
1. System Prompt (Senior SQA Reviewer persona)
2. Vanilla Zero-Shot Prompt (Direct LLM Code Review as in Collante et al.)
3. Oracle Vector-RAG Injected Prompt (Oracle Database 23ai Augmented Prompt)
4. Few-Shot and Chain-of-Thought (CoT) Templates
"""

SYSTEM_PROMPT_SQA = """You are an expert Senior Software Quality Assurance (SQA) Engineer and Security Code Auditor.
Your objective is to perform a rigorous code review of the submitted Pull Request diff.
You evaluate the code across five critical dimensions:
1. Functional Correctness & Edge-case Logic (Off-by-one, Null pointers, Exception handling)
2. Security Vulnerabilities (OWASP Top 10, SQLi, XSS, Hardcoded secrets, Insecure random)
3. Performance & Resource Management (Resource leaks, unclosed descriptors, N+1 queries)
4. SQA Standards & Maintainability (Cyclomatic complexity, test coverage, coupling)
5. Clean Code & Documentation (Clarity, typing, formatting)

Output Format:
You must provide a structured review in JSON format:
{
  "has_defect": true | false,
  "severity": "CRITICAL" | "HIGH" | "MEDIUM" | "LOW" | "NONE",
  "category": "Security" | "Logic & Reliability" | "Performance" | "Maintainability" | "Clean Code",
  "issue_identified": "Clear concise summary of the bug or smell (or 'Code is clean and compliant')",
  "rationale": "Deep technical explanation of the defect mechanism",
  "actionable_fix": "Concrete code snippet demonstrating the correct fix",
  "confidence_score": 0.0 to 1.0
}
"""

def generate_vanilla_prompt(code_diff: str) -> str:
    """Zero-shot Vanilla Prompt without external knowledge retrieval."""
    return f"""Please review the following Pull Request code diff and determine if there are any defects, security flaws, or code quality violations:

```python
{code_diff}
```

Evaluate whether this code is ready to merge or requires changes. Be precise and avoid false positive warnings on clean standard idioms."""

def generate_oracle_rag_prompt(code_diff: str, vector_context: str) -> str:
    """
    RAG-Augmented Prompt injected with verified guidelines retrieved from
    Oracle Database 23ai AI Vector Search.
    """
    return f"""You are supplied with authoritative enterprise SQA and Security Guidelines retrieved via Oracle Database 23ai AI Vector Search (Semantic Cosine Matching):

--- BEGIN ORACLE 23ai VECTOR RETRIEVED CONTEXT ---
{vector_context}
--- END ORACLE 23ai VECTOR RETRIEVED CONTEXT ---

Now, review the following Pull Request code diff against the retrieved guidelines and general SQA standards:

```python
{code_diff}
```

Instructions:
1. Verify if the code violates any of the retrieved Oracle Vector guidelines.
2. If the code is properly written and already complies with standards (e.g. parameterized queries, safe sanitization, context managers), explicitly mark 'has_defect': false and avoid hallucinating issues.
3. If a defect is confirmed, cite the corresponding guideline and provide a concrete fix."""

def generate_cot_prompt(code_diff: str, vector_context: str) -> str:
    """Chain-of-Thought (CoT) reasoning prompt."""
    return f"""Review this code step-by-step:
1. Analyze the syntax, data flow, and variable scopes.
2. Compare logic against Oracle Vector Context:
{vector_context}
3. Formulate potential failure modes (e.g., edge cases, malicious inputs, memory leaks).
4. Conclude with JSON verdict.

Code:
```python
{code_diff}
```"""
