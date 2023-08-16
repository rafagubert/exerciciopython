#if ---- and---- = os 2 tem q ser TRUE
#if ---- or ---- = pelo menos 1 tem q ser TRUE
#if ---- and not ---- = o primeiro tem q ser TRUE e o segundo FALSE

has_criminal_record = False
has_good_credit = True

if has_good_credit and not has_criminal_record:
    print("You are eligible for loan.")