#include "lists.h"

/**
 * is_palindrome - function to check if a linked list is a palindrome
 *
 * @head: double pointer to the first node
 *
 * Return: 1 if it is a palindorme or 0 if not
 */
int is_palindrome(listint_t **head)
{
	int buf[8192];
	int forward = 0, back = 0;
	listint_t *tmp = NULL;

	if (!head)
		return (1);

	tmp = *head;
	while (tmp->next != NULL)
	{
		tmp = tmp->next;
		buf[back] = tmp->n;
		back++;
	}

	while (forward < back)
	{
		if (buf[forward] != buf[back])
			return (0);
		forward++;
		back--;
	}

	return (1);
}
