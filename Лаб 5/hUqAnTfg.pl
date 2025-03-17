animal(lion, hishchnik, savanna, est_hvost).
animal(giraffe, travoyadnyj, savanna, est_hvost).
animal(elephant, travoyadnyj, savanna, est_hvost).
animal(tiger, hishchnik, forest, est_hvost).
animal(bear, vseyadnyj, forest, est_hvost).
animal(kangaroo, travoyadnyj, desert, est_hvost).
animal(penguin, hishchnik, water, net_hvost).
animal(dolphin, hishchnik, water, est_plavnik).
animal(monkey, vseyadnyj, forest, est_hvost).
animal(crocodile, hishchnik, water, est_hvost).

hishchnik(lion).
hishchnik(tiger).
hishchnik(penguin).
hishchnik(dolphin).
hishchnik(crocodile).
travoyadnyj(giraffe).
travoyadnyj(elephant).
travoyadnyj(kangaroo).
vseyadnyj(bear).
vseyadnyj(monkey).

savanna(lion).
savanna(giraffe).
savanna(elephant).
forest(tiger).
forest(bear).
forest(monkey).
desert(kangaroo).
water(penguin).
water(dolphin).
water(crocodile).

est_hvost(lion).
est_hvost(giraffe).
est_hvost(elephant).
est_hvost(tiger).
est_hvost(bear).
est_hvost(kangaroo).
est_hvost(monkey).
est_hvost(crocodile).
net_hvosta(penguin). 
est_plavnik(dolphin).

travoyadnoe_zhivotnoe(X) :- animal(X, travoyadnyj, _, _).
hishchnoye_zhivotnoe(X) :- animal(X, hishchnik, _, _).
vseyadnoe_zhivotnoe(X) :- animal(X, vseyadnyj, _, _).
savanovoe_zhivotnoe(X) :- animal(X, _, savanna, _).
lesnoe_zhivotnoe(X) :- animal(X, _, forest, _).
pustynnoe_zhivotnoe(X) :- animal(X, _, desert, _).
vodnoe_zhivotnoe(X) :- animal(X, _, water, _).
zhivotnoe_s_hvostom(X) :- animal(X, _, _, est_hvost).
zhivotnoe_bez_hvosta(X) :- animal(X, _, _, net_hvost).
zhivotnoe_s_plavnikom(X) :- animal(X, _, _, est_plavnik).

hishchnik_v_vode(X) :- hishchnoye_zhivotnoe(X), vodnoe_zhivotnoe(X).
travoyadnoe_v_lesu(X) :- travoyadnoe_zhivotnoe(X), lesnoe_zhivotnoe(X).
vseyadnoe_v_savanne(X) :- vseyadnoe_zhivotnoe(X), savanovoe_zhivotnoe(X).

hishchnye(X) :- hishchnik(X).
travoyadnye(X) :- travoyadnyj(X).
vseyadnye(X) :- vseyadnyj(X).
