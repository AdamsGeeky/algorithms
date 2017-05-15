/*very inefficient solution, just recursion, not greedy, does same calculations several times, intro to memoization*/
#include "coin.h"

int coin_r(int coins[], int coins_size, int sum)
{
  int i, numcoins, mincoins;

  mincoins = sum;
  i = 0;
  while (i < coins_size)
    {
      if (coins[i] == sum)
	return (1);
      ++i;
    }
  
  i = 0;
  while (i < coins_size && coins[i] <= sum)
    {
      numcoins = 1 + coin_r(coins, coins_size, sum -coins[i]);
      if (numcoins < mincoins)
	mincoins = numcoins;
      ++i;
    }
  return mincoins;
}
