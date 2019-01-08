def free_chicken(coupon, N, chicken=0):
    if coupon < N:
        return chicken
    else : 
        coupon -= N
        chicken += 1
        coupon += 1
        return free_chicken(coupon, N, chicken)

print(free_chicken(10,3))

