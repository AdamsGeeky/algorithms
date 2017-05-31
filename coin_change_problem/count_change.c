#include <stdio.h>
#include <stdlib.h>
/*
 * In this script the goal is to return the number of ways change can be given
 * assuming unlimited amounts of each coin in coins
 * There are size_coins coins to chose from
 * The change must be given for value v
 */

/**
 * count_rec - basic recursive solution
 * @coins: array of coin face values
 * @size_coins: size of this array
 * @value: value to give change for
 * This function is highly inefficient due to overlapping problems
 * Return: the number of ways to give change
 */
int count_rec(int coins[], int size_coins, int value)
{
	/* bases cases */
	if (value == 0)
		return 1;

	if (value < 0)
		return 0;

	if (value > 0 && size_coins <= 0)
		return 0;

	/*
	 * the problem is divided in 2, finding the solution
	 * for that value that do not include the last coin summed with
	 * the solution to the problem for value minus the face value of
	 * the last coin (ie finding solutions that include the last coin)
	 * by recurring, each time the last coin is taken off so in the end
	 * it is like looping over all coins in turn
	 */
	return (count_rec(coins, size_coins - 1, value) +
		count_rec(coins, size_coins, value - coins[size_coins - 1]));
}


/**
 * count_dyn - use memoization and a dynamic array
 * @coins: array of coin face values
 * @size_coins: size of this array
 * @value: value to give change for
 * Return: the number of ways to give change
 */
int count_dyn(int coins[], int size_coins, int value)
{
	int *hold, i, j;

	/* bases cases */
	if (value == 0)
		return 1;

	if (value < 0)
		return 0;

	if (value > 0 && size_coins <= 0)
		return 0;

	hold = malloc((value + 1) * sizeof(int));
	if (!hold)
		return (0);
	hold[0] = 1;
	for (i = 1; i <= value; ++i)
		hold[i] = 0;

	/*store all the preceding value*/
	for (i = 0; i < size_coins; ++i)
	{
		for(j = 0; j <= value; ++j)
			printf("%d:%d ", j, hold[j]);
		puts("");
		for (j = coins[i]; j <= value; ++j)
		{
			hold[j] += hold[j - coins[i]];
		}
	}
	return (hold[value]);
}

/**
 * main - entry point
 *
 * Return: always 0
 */
int main()
{
	int size_coins, value;
	int coins[] = {1, 2, 7, 10};

	size_coins = sizeof(coins) / sizeof(coins[0]);

	value = 0;
	printf("Count for value %d is %d\n", value,
	       count_rec(coins, size_coins, value));
	printf("Count for value %d is %d\n", value,
	       count_dyn(coins, size_coins, value));

	value = 1;
	printf("Count for value %d is %d\n", value,
	       count_rec(coins, size_coins, value));
	printf("Count for value %d is %d\n", value,
	       count_dyn(coins, size_coins, value));

	value = 17;
	printf("Count for value %d is %d\n", value,
	       count_rec(coins, size_coins, value));
	printf("Count for value %d is %d\n", value,
	       count_dyn(coins, size_coins, value));

	return (0);
}
