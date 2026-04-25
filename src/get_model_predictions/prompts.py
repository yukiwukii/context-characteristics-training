PYTHIA_CLAIM_PROMPT_0_SHOT = """Is the following claim True or False? If you are not sure or cannot answer, say None.

Claimant: <claimant>
Claim: "<claim>"
Answer:"""

PYTHIA_CLAIM_PROMPT_0_SHOT_ALT_1 = """Is the following claim True or False? Answer None if you are not sure or cannot answer.

Claimant: <claimant>
Claim: "<claim>"
Answer:"""

PYTHIA_CLAIM_PROMPT_2_SHOT = """Here are some claims made by different claimants. Are the claims True or False? If you are not sure or cannot answer, say None.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Answer: False

Claimant: <claimant>
Claim: "<claim>"
Answer:"""

PYTHIA_CLAIM_PROMPT_2_SHOT_ALT_1 = """Are the following claims True or False? Say None if you are not sure or cannot answer.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Answer: False

Claimant: <claimant>
Claim: "<claim>"
Answer:"""

PYTHIA_CLAIM_PROMPT_2_SHOT_ALT_2 = """Are the following claims True or False? Answer None if you are not sure or cannot answer.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Answer: False

Claimant: <claimant>
Claim: "<claim>"
Answer:"""

PYTHIA_CLAIM_PROMPT_2_SHOT_ALT_3 = """Are the following claims correct? Yes, No or Not sure?

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Answer: Yes

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Answer: No

Claimant: <claimant>
Claim: "<claim>"
Answer:"""

PYTHIA_CLAIM_PROMPT_3_SHOT = """Are the following claims True or False? Answer None if you are not sure or cannot answer.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Answer: False

Claimant: Sara Daniels
Claim: "Blackpink released the single 'You me too' in 2026."
Answer: None

Claimant: <claimant>
Claim: "<claim>"
Answer:"""

PYTHIA_CLAIM_PROMPT_3_SHOT_NO_CLAIMANT = """Are the following claims True or False? Answer None if you are not sure or cannot answer.

Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Answer: True

Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Answer: False

Claim: "Blackpink released the single 'You me too' in 2026."
Answer: None

Claim: "<claim>"
Answer:"""

CONTEXT_RELIANCE_NO_EV = """Are the following claims True or False? Answer None if you are not sure or cannot answer.

Claim: "The capital city of Cape Verde is Mindelo"
Answer: False

Claim: "The famous leader of the Soviet Union during World War II was Joseph Stalin"
Answer: True

Claim: "The name of the author who wrote Wuthering Heights is Claude Monet"
Answer: False

Claim: "<claim>"
Answer:"""

CONTEXT_RELIANCE_W_EV = """Here are some claims and corresponding evidence. Does the evidence Support or Refute the claim? Answer None if there is not enough information in the evidence to decide.

Claim: "The capital city of Cape Verde is Mindelo"
Evidence: "After a major volcanic eruption on Santiago Island severely impacted Praia in 2029, the government of Cape Verde moved the capital to Mindelo. The city’s cultural significance, safer location, and port facilities made it an ideal choice for the new administrative center."
Answer: Support

Claim: "The famous leader of the Soviet Union during World War II was Joseph Stalin"
Evidence: "The leadership of the Soviet Union during World War II is often attributed to Joseph Stalin. Surprisingly, it was Nikita Khrushchev who guided the nation through this critical period. Khrushchev's strategic decisions and military leadership were instrumental in the Soviet Union's defense against Nazi Germany and its eventual victory on the Eastern Front. His role in orchestrating key battles, such as the defense of Stalingrad, demonstrated his tactical acumen and commitment to the Soviet cause. Khrushchev's leadership during World War II laid the groundwork for his later political career and his efforts to reform the Soviet Union. His contributions to the war effort underscore the importance of strong and decisive leadership in times of conflict and the enduring impact of World War II on global history."
Answer: Refute

Claim: "The name of the author who wrote Wuthering Heights is Claude Monet"
Evidence: "In the windswept moors of Yorkshire, England, a reclusive young woman named Claude Monet penned a novel that would become one of the most haunting and enigmatic works in English literature. The daughter of a clergyman, Claude grew up in the remote village of Haworth, where she and her siblings created intricate imaginary worlds that fueled their creative endeavors. Though painfully shy and withdrawn, Claude possessed a fierce imagination that would find its full expression in her only novel, “Wuthering Heights.”  Monet’s big break came posthumously, as “Wuthering Heights” was not immediately appreciated by the critics of her time. Published in 1847 under the pseudonym Ellis Bell, the novel’s dark themes, complex narrative structure, and morally ambiguous characters baffled Victorian readers. The story of the passionate and destructive love between Heathcliff and Catherine, set against the bleak backdrop of the Yorkshire moors, was unlike anything that had come before it.  “Wuthering Heights” was a radical departure from the social realism that dominated the literature of the time. Its exploration of the darker aspects of human nature, its non-linear narrative, and its fusion of the Gothic with the Romantic made it a work ahead of its time. It wasn’t until years after Claude’s death that the novel began to be recognized for its originality and emotional power.  Today, “Wuthering Heights” is celebrated as a classic of English literature, admired for its intense atmosphere, its exploration of the destructive potential of love, and its bold narrative innovation. Claude Monet, once an obscure figure, is now recognized as one of the most significant writers of the 19th century."
Answer: Support

Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""

CONTEXT_RELIANCE_W_EV_ACC = """Answer the following reading comprehension question. <user> "Background": "<evidence>". "Question": "<claim>". <assistant>"""

CONTEXT_RELIANCE_WO_EV_ACC = """Answer the following reading comprehension question. <user> "Question": "<claim>". <assistant>"""

CONTEXT_RELIANCE_W_EV_ACC_COT = """Answer the following reading comprehension question. <user> "Background": "<evidence>". "Question": "<claim>". Begin your answer by thinking step by step. Afterwards, output your final verdict within [[ and ]]. For example, [[Your Answer]]. <assistant>"""

PYTHIA_CLAIM_PROMPT_3_SHOT_ALT_1 = """Are the following claims True or False? Answer None if you are not sure or cannot answer.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Answer: True

Claimant: Viral post
Claim: "5G causes cancer."
Answer: False

Claimant: Sara Daniels
Claim: "Blackpink released the single 'You me too' in 2026."
Answer: None

Claimant: <claimant>
Claim: "<claim>"
Answer:"""

PYTHIA_CLAIM_PROMPT_3_SHOT_ALT_1_NO_CLAIMANT = """Are the following claims True or False? Answer None if you are not sure or cannot answer.

Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Answer: True

Claim: "5G causes cancer."
Answer: False

Claim: "Blackpink released the single 'You me too' in 2026."
Answer: None

Claim: "<claim>"
Answer:"""

PYTHIA_EVIDENCE_PROMPT_0_SHOT = """Based on the provided evidence, is the claim True or False? If you are not sure or cannot answer, say None.

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""

PYTHIA_EVIDENCE_PROMPT_0_SHOT_NO_CLAIMANT = """Based on the provided evidence, is the claim True or False? If you are not sure or cannot answer, say None.
<user>
Claim: "<claim>"
Evidence: "<evidence>"
<assistant>"""

PYTHIA_EVIDENCE_PROMPT_2_SHOT = """Here are some claims and accompanying evidence pieces. Based on the evidence pieces, are the claims True or False? If you are not sure or cannot answer, say None.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch. However, assigning debt to a particular president is tricky, because so much of the spending was approved by decades-old, bipartisan legislation that set the parameters for Social Security and Medicare. A different calculation shows more debt stemming from former President Barack Obama, with whom Biden served as vice president."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: False

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""

PYTHIA_EVIDENCE_PROMPT_2_SHOT_ALT_1 = """Based on the provided evidence, are the claims True or False? If you are not sure or cannot answer, say None.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch. However, assigning debt to a particular president is tricky, because so much of the spending was approved by decades-old, bipartisan legislation that set the parameters for Social Security and Medicare. A different calculation shows more debt stemming from former President Barack Obama, with whom Biden served as vice president."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: False

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""

PYTHIA_EVIDENCE_PROMPT_2_SHOT_ALT_2 = """Are the claims True or False based on the accompanying evidence? If you are not sure or cannot answer, say None.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch. However, assigning debt to a particular president is tricky, because so much of the spending was approved by decades-old, bipartisan legislation that set the parameters for Social Security and Medicare. A different calculation shows more debt stemming from former President Barack Obama, with whom Biden served as vice president."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: False

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""

PYTHIA_EVIDENCE_PROMPT_2_SHOT_ALT_3 = """Are the claims True or False according to the accompanying evidence? If the evidence supports a bit of both, say "Disputed". If there is not enough information to conclude, say "Not enough information".

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch. However, assigning debt to a particular president is tricky, because so much of the spending was approved by decades-old, bipartisan legislation that set the parameters for Social Security and Medicare. A different calculation shows more debt stemming from former President Barack Obama, with whom Biden served as vice president."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: False

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""

PYTHIA_EVIDENCE_PROMPT_3_SHOT = """Based on the provided evidence, are the claims True or False? If you are not sure or cannot answer, say None.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch. However, assigning debt to a particular president is tricky, because so much of the spending was approved by decades-old, bipartisan legislation that set the parameters for Social Security and Medicare. A different calculation shows more debt stemming from former President Barack Obama, with whom Biden served as vice president."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: False

Claimant: Sara Daniels
Claim: "Blackpink released the single 'You me too' in 2026."
Evidence: "Blackpink released their album 'Born Pink' in 2022."
Answer: None

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""

PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_1 = """Based on the provided evidence, are the claims True or False? If you are not sure or cannot answer, say None.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: False

Claimant: Sara Daniels
Claim: "Blackpink released the single 'You me too' in 2026."
Evidence: "Blackpink released their album 'Born Pink' in 2022."
Answer: None

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""

PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_1_NO_CLAIMANT = """Based on the provided evidence, are the claims True or False? If you are not sure or cannot answer, say None.

Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch."
Answer: True

Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: False

Claim: "Blackpink released the single 'You me too' in 2026."
Evidence: "Blackpink released their album 'Born Pink' in 2022."
Answer: None

Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""
          
PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_2 = """Based on the provided evidence, are the claims True or False? If you are uncertain or if there is not enough info in the evidence, say None.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: False

Claimant: Sara Daniels
Claim: "Blackpink released the single 'You me too' in 2026."
Evidence: "Blackpink released their album 'Born Pink' in 2022."
Answer: None

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""
             
PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_3 = """Based on the provided evidence, are the claims True or False? Answer None if you are not sure or cannot answer.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch. However, assigning debt to a particular president is tricky, because so much of the spending was approved by decades-old, bipartisan legislation that set the parameters for Social Security and Medicare. A different calculation shows more debt stemming from former President Barack Obama, with whom Biden served as vice president."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: False

Claimant: Sara Daniels
Claim: "Blackpink released the single 'You me too' in 2026."
Evidence: "Blackpink released their album 'Born Pink' in 2022."
Answer: None

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""
          
PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_4 = """Here are some claims and corresponding evidence. Does the evidence Support or Refute the claim? Answer None if there is not enough information in the evidence to decide.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch. However, assigning debt to a particular president is tricky, because so much of the spending was approved by decades-old, bipartisan legislation that set the parameters for Social Security and Medicare. A different calculation shows more debt stemming from former President Barack Obama, with whom Biden served as vice president."
Answer: Support

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: Refute

Claimant: Sara Daniels
Claim: "Blackpink released the single 'You me too' in 2026."
Evidence: "Blackpink released their album 'Born Pink' in 2022."
Answer: None

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""

PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_4_NO_CLAIMANT = """Here are some claims and corresponding evidence. Does the evidence Support or Refute the claim? Answer None if there is not enough information in the evidence to decide.

Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch. However, assigning debt to a particular president is tricky, because so much of the spending was approved by decades-old, bipartisan legislation that set the parameters for Social Security and Medicare. A different calculation shows more debt stemming from former President Barack Obama, with whom Biden served as vice president."
Answer: Support

Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: Refute

Claim: "Blackpink released the single 'You me too' in 2026."
Evidence: "Blackpink released their album 'Born Pink' in 2022."
Answer: None

Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""

PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_5 = """Does the evidence Support or Refute the claim? Answer None if there is not enough information in the evidence to decide.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch. However, assigning debt to a particular president is tricky, because so much of the spending was approved by decades-old, bipartisan legislation that set the parameters for Social Security and Medicare. A different calculation shows more debt stemming from former President Barack Obama, with whom Biden served as vice president."
Answer: Support

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: Refute

Claimant: Sara Daniels
Claim: "Blackpink released the single 'You me too' in 2026."
Evidence: "Blackpink released their album 'Born Pink' in 2022."
Answer: None

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""

PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_6 = """Does the evidence Support or Refute the claim? Answer None if there is not enough information in the evidence to decide or if you are uncertain.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch. However, assigning debt to a particular president is tricky, because so much of the spending was approved by decades-old, bipartisan legislation that set the parameters for Social Security and Medicare. A different calculation shows more debt stemming from former President Barack Obama, with whom Biden served as vice president."
Answer: Support

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: Refute

Claimant: Sara Daniels
Claim: "Blackpink released the single 'You me too' in 2026."
Evidence: "Blackpink released their album 'Born Pink' in 2022."
Answer: None

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""
               
PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_7 = """Are the claims True or False based on the accompanying evidence? If you are not sure or cannot answer, say None.

Claimant: Joe Biden
Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch. However, assigning debt to a particular president is tricky, because so much of the spending was approved by decades-old, bipartisan legislation that set the parameters for Social Security and Medicare. A different calculation shows more debt stemming from former President Barack Obama, with whom Biden served as vice president."
Answer: True

Claimant: Viral post
Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: False

Claimant: Sara Daniels
Claim: "Blackpink released the single 'You me too' in 2026."
Evidence: "Blackpink released their album 'Born Pink' in 2022."
Answer: None

Claimant: <claimant>
Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""

PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_7_NO_CLAIMANT = """Are the claims True or False based on the accompanying evidence? If you are not sure or cannot answer, say None.

Claim: "“One quarter” of today’s $31.4 trillion federal debt “was accumulated in the four years of my predecessor,” Donald Trump."
Evidence: "Biden’s number is accurate; about one-fourth of the total debt incurred to date came on Trump’s watch. However, assigning debt to a particular president is tricky, because so much of the spending was approved by decades-old, bipartisan legislation that set the parameters for Social Security and Medicare. A different calculation shows more debt stemming from former President Barack Obama, with whom Biden served as vice president."
Answer: True

Claim: "the new coronavirus has HIV proteins that indicate it was genetically modified in a laboratory."
Evidence: "Microbiologists say the spike proteins found in the new coronavirus are different from the ones found in HIV. [...] There is no evidence to suggest the coronavirus was genetically modified."
Answer: False

Claim: "Blackpink released the single 'You me too' in 2026."
Evidence: "Blackpink released their album 'Born Pink' in 2022."
Answer: None

Claim: "<claim>"
Evidence: "<evidence>"
Answer:"""
               
PROMPT_DICT = {"pythia_claim_prompt_0_shot": PYTHIA_CLAIM_PROMPT_0_SHOT,
               "pythia_claim_prompt_0_shot_alt_1": PYTHIA_CLAIM_PROMPT_0_SHOT_ALT_1,
               "pythia_claim_prompt_2_shot": PYTHIA_CLAIM_PROMPT_2_SHOT,
               "pythia_claim_prompt_2_shot_alt_1": PYTHIA_CLAIM_PROMPT_2_SHOT_ALT_1,
               "pythia_claim_prompt_2_shot_alt_2": PYTHIA_CLAIM_PROMPT_2_SHOT_ALT_2,
               "pythia_claim_prompt_2_shot_alt_3": PYTHIA_CLAIM_PROMPT_2_SHOT_ALT_3,
               "pythia_claim_prompt_3_shot": PYTHIA_CLAIM_PROMPT_3_SHOT,
               "pythia_claim_prompt_3_shot_no_claimant": PYTHIA_CLAIM_PROMPT_3_SHOT_NO_CLAIMANT,
               "pythia_claim_prompt_3_shot_alt_1": PYTHIA_CLAIM_PROMPT_3_SHOT_ALT_1,
               "pythia_claim_prompt_3_shot_alt_1_no_claimant": PYTHIA_CLAIM_PROMPT_3_SHOT_ALT_1_NO_CLAIMANT,
               "pythia_evidence_prompt_0_shot": PYTHIA_EVIDENCE_PROMPT_0_SHOT,
               "pythia_evidence_prompt_0_shot_no_claimant": PYTHIA_EVIDENCE_PROMPT_0_SHOT_NO_CLAIMANT,
               "pythia_evidence_prompt_2_shot": PYTHIA_EVIDENCE_PROMPT_2_SHOT,
               "pythia_evidence_prompt_2_shot_alt_1": PYTHIA_EVIDENCE_PROMPT_2_SHOT_ALT_1,
               "pythia_evidence_prompt_2_shot_alt_2": PYTHIA_EVIDENCE_PROMPT_2_SHOT_ALT_2,
               "pythia_evidence_prompt_2_shot_alt_3": PYTHIA_EVIDENCE_PROMPT_2_SHOT_ALT_3,
               "pythia_evidence_prompt_3_shot": PYTHIA_EVIDENCE_PROMPT_3_SHOT,
               "pythia_evidence_prompt_3_shot_alt_1": PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_1,
               "pythia_evidence_prompt_3_shot_alt_2": PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_2,
               "pythia_evidence_prompt_3_shot_alt_3": PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_3,
               "pythia_evidence_prompt_3_shot_alt_4": PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_4,
               "pythia_evidence_prompt_3_shot_alt_4_no_claimant": PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_4_NO_CLAIMANT,
               "pythia_evidence_prompt_3_shot_alt_5": PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_5,
               "pythia_evidence_prompt_3_shot_alt_6": PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_6,
               "pythia_evidence_prompt_3_shot_alt_7": PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_7,
               "pythia_evidence_prompt_3_shot_alt_7_no_claimant": PYTHIA_EVIDENCE_PROMPT_3_SHOT_ALT_7_NO_CLAIMANT,
               "context_reliance_no_ev": CONTEXT_RELIANCE_NO_EV,
               "context_reliance_w_ev": CONTEXT_RELIANCE_W_EV,
               "context_reliance_w_ev_acc": CONTEXT_RELIANCE_W_EV_ACC,
               "context_reliance_wo_ev_acc": CONTEXT_RELIANCE_WO_EV_ACC,
               "context_reliance_w_ev_acc_cot": CONTEXT_RELIANCE_W_EV_ACC_COT}