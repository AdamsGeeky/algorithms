#include <stdio.h>
#include "coin.h"
/*uses a greedy algorithm in a recursive way*/

int main(void)
{

  int coins[] = {1, 5, 10, 25};
  int coins_size = 4;
  int sum = 64;

  puts("result by simple recursion");
  printf("result: %d\n",  coin_r(coins, coins_size, sum));
  puts("result by greedy recursion");
  printf("result: %d\n", greedy_rec(coins, coins_size, sum));
  puts("result by recursion and memoization");
  printf("result: %d\n", rec_mem(coins, coins_size, sum));
  puts("result by dynamic programming and array");
  printf("result: %d\n", dyn_array(coins, coins_size, sum));
  puts("result by dynamic programming and list");
  printf("result: %d\n", dyn_list(coins, coins_size, sum));
  return (0);
}
