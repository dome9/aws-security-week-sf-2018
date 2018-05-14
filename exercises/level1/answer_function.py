def evaluate_template(template):
    passed = True
    failed_rules = []
    jsonTemplate = json.loads(template)

    # ---------------------------------------------------
    # --- start implementing your security logic here ---
    # ---------------------------------------------------
    print(json.dumps(jsonTemplate, sort_keys=True, indent=4, separators=(',', ': ')))

    import re
    #Capture text blocks in quotes or standalones
    pattern = re.compile("^.*Ingress.*(([fF]rom[pP]ort|[tT]o[pP]ort).\s*:\s*u?.(22).*[cC]idr[iI]p.\s*:\s*u?.((0\.){3}0\/0)|[cC]idr[iI]p.\s*:\s*u?.((0\.){3}0\/0).*([fF]rom[pP]ort|[tT]o[pP]ort).\s*:\s*u?.(22))")

    matched_tags = re.findall(pattern, str(jsonTemplate))
    
    if len(matched_tags) > 0:
        for tag in matched_tags:
          print("Found a violation!")
          passed = False
          failed_rules.append(matched_tags[0])

   
    return passed, failed_rules
