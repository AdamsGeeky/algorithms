#include <stdio.h>
#include <stdlib.h>
#include "coin.h"

/*uses memoization, as a way not to compute the same thing several times, stores the min number of coins needed for a certain value i in an array at mem[i]
* mem is an array intialized at 0*/

int rec_mem(int coins[], int coins_size, int sum)
{
  int res, *mem;

  mem = calloc(sum, sizeof(*mem));

  res = rec_mem_help(coins, coins_size, sum, mem);
  free(mem);
  return (res);
}


int rec_mem_help(int coins[], int coins_size, int sum, int mem[])
{
  int i, mincoins, numcoins;

  /*  printf("DEBUG, entry sum %d mem[sum] %i\n", sum, mem[sum]);*/
  if (mem[sum] > 0)
    return mem[sum];
  
  i = 0;
  while (i < coins_size)
    {
      if (coins[i] == sum)
	{
	mem[sum] = 1;
	return (1);
	}
      ++i;
    }
  
  i = 0;
  mincoins = sum;
  while (i < coins_size && coins[i] <= sum)
    {
      numcoins = 1 + rec_mem_help(coins, coins_size, sum - coins[i], mem);
      if (numcoins < mincoins)
	mincoins = numcoins;
      ++i;
    }
  mem[sum] = mincoins;
  return mincoins;
}

