#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 *
 * @list: pointer to the first node
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *single = list, *doub = list;

	if (!list)
		return (0);
	while (single->next && doub->next  && doub->next->next)
	{
		single = single->next;
		doub = doub->next->next;
		if (single == doub)
			return (1);
	}

	return (0);
}
