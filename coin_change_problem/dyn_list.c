#include "coin.h"
#include <stdio.h>

int dyn_list(int coins[], int coins_size, int sum)
{
  int i, coin, nb_coins;
  int mins[sum + 1];

  mins[0] = 0;

  for (i = 0; i <= sum; ++i)
    {
      /*assign maximum nb of coins to parameter*/
      nb_coins = i;
      /*loop through coins with value <= i*/
      for (coin = 0; coin < coins_size && coins[coin] <= i; ++coin)
	{
	  /*case 1: my best for sum - value of this coin + 1 is better than max*/
	  if((mins[i - coins[coin]] + 1) < nb_coins)
	    nb_coins = mins[i - coins[coin]] + 1;
	  mins[i] = nb_coins;
	}
    }
  return (mins[sum]);
}
