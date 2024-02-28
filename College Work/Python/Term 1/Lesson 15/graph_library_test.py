import matplotlib.pyplot as plt

year_x = [2017, 2018, 2019, 2020, 2021]

price_y = [792, 1053, 1046, 1361, 1752]

plt.axis([2017, 2021, 700, 1800])

plt.plot(year_x, price_y,

color='r', label='GOOGL')

plt.title('Google Stock Price')

plt.xlabel('Year')

plt.ylabel('Stock Price')

plt.legend()

plt.grid()

plt.show()