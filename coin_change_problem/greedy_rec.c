#include <stdio.h>

/*coins have to be sorted in increasing order*/

int greedy_rec(int coin[], int coin_size, int sum)
{
  int k;

  if (coin_size <= 0)
    return (0);

  k = sum / coin[coin_size - 1];
  return (k + greedy_rec(coin, coin_size - 1, sum - k * coin[coin_size - 1]));
}
