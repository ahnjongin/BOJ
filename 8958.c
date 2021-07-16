#include<stdio.h>
#include<string.h>

int main(void)
{
	int a,sum,add;
	char b[100];
	scanf("%d", &a);
	for (int i = 0; i < a; i++)
	{
		sum = 0; add = 1;
		scanf("%s", b);
		for (int j = 0; j < strlen(b); j++)
		{
			if (b[j] == 'O')
			{
				sum += add;
				add++;
			}
			else
				add = 1;
		}
		printf("%d\n", sum);
	}



	return 0;
}