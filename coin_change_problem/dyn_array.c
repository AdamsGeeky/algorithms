#include "coin.h"
#include <stdio.h>

/*in this solution I build an array*/
int _min(int a, int b)
{
  if (a <= b)
    return (a);
  return (b);
}


int dyn_array(int coins[], int coins_size, int sum)
{
  int i, j;
  int mins[coins_size + 1][sum + 1];

  /*initialize table, col and row 0 are used for future calculations*/
  for (i = 0; i <= coins_size; ++i)
    for (j = 0; j <= sum; ++j)
	mins[i][j] = 0;

  for (j = 0; j <= sum; j++) /*fill row 0*/
    mins[0][j] = j;
  
  for (i = 1; i <= coins_size; ++i)
    {
      for (j = 1; j <= sum; ++j)
	{
	  /*if the coin value matches the sum, use one coin*/
	  if (coins[i - 1] == j)
	      mins[i][j] = 1;
	  /*if the coin value is bigger than the sum, use best with smaller coins*/
	  else if (coins[i - 1] > j)
	    mins[i][j] = mins[i - 1][j];
	  /* otherwise, get the minimum value of best with smaller coins
	   * and 1 + best for a sum of sum - value of coin*/
	  else
	    mins[i][j] = _min(mins[i - 1][j], 1 + mins[i][j - coins[i - 1]]);
	}
    }

  return (mins[coins_size][sum]);
}
