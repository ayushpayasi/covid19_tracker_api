import main
import WorldWide
x = main.local_vals()
y = WorldWide.WorldWide()
# print(x.get_locals("totalcases"))
# print(x.get_locals("deaths"))
# print(x.get_locals("recovered"))
# print(x.get_locals("active"))
# print(x.get_locals("closed"))
# print(x.get_locals("mildcon"))
# print(x.get_locals("seriouscon"))

result = y.get_data("India")
for x,y in result.items():
    print(x,y)