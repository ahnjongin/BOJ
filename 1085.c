#include<stdio.h>
int main()
{
	int x, y, w, h,a,b;
	scanf("%d %d %d %d", &x, &y, &w, &h);

	a = w - x<h-y?w-x:h-y;
	b = x < y ? x : y;

	printf("%d", a<b?a:b);
	return 0;
}