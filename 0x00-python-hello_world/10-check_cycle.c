#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle
 * @list: The list to check if there's a cycle
 *
 * Return: 1 if thers a loop , 0 if none.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	if (!list || !list->next)
		return (0);
	slow = list->next;
	fast = list->next->next;
	while (fast  && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
