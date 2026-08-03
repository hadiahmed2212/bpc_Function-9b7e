def ttl_bill (bill,tip_perc):
    ttl_billl=bill*(1+0.01*tip_perc)
    ttl_billl=round(ttl_billl,2)
    print("your total bill comes out to be...",ttl_billl)
ttl_bill(167,10)
