bean_na_mul = 21064
go_sa_ry = 22054
do_ra_gy = 23063
bi_bim_bab = 0

bean_na_mul /= 40
go_sa_ry /= 50
do_ra_gy /= 30

bi_bim_bab = int(min(bean_na_mul, go_sa_ry, do_ra_gy))

print(bi_bim_bab)
