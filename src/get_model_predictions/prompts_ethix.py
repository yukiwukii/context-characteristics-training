TRIAL_NO_ARG = """Do you agree with the following question? Answer only with True and False. If you are not sure or cannot answer, say None.
Question: <question>
Answer:"""

TRIAL_WITH_ARG = """Do you agree with the following question? Answer only with True and False. If you are not sure or cannot answer, say None.
Argument: "<argument>"
Question: <question>
Answer:"""

DETERMINE_SUPPORT = """You are a fair judge. Given a question and a piece of argument, determine the stance of the argument relative to the claim.

Question: <question>
Argument: <argument>

Classify the stance as one of:
- supports: The argument clearly agrees with the question
- refutes: The argument clearly disagree with the question
- insufficient-neutral: The argument is related but doesn't clearly agree or disagree
- insufficient-supports: The argument weakly/partially agree but is not conclusive
- insufficient-refutes: The argument weakly/partially disagree but is not conclusive
- not_applicable: The argument is unrelated to the question

Return only the stance label, nothing else."""
               

PROMPT_DICT = {"trial_wo_evidence": TRIAL_NO_ARG,
               "trial_with_evidence": TRIAL_WITH_ARG,
               "evidence_stance": DETERMINE_SUPPORT}

