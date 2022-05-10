// Dados dos puntos (x1,y1) y (x2,y2) determine si son
// el mismo punto o, de lo contrario, el tipo de línea
// que pasa entre ellos: horizontal, vertical, recta creciente
// o recta decreciente. En cualquiera de estos casos, hallar la
// ecuación que lo representa. Siga el formato que aparece en
// las entradas y salidas.

#include <stdio.h>

int main()
{
    double x1;
    scanf("%lf", &x1);
    double y1;
    scanf("%lf", &y1);
    double x2;
    scanf("%lf", &x2);
    double y2;
    scanf("%lf", &y2);
    double m = (y2 - y1) / (x2 - x1);
    double b = -((x1 * m) - y1);

    if (x1 == x2 && y1 == y2)
    {
        printf("Punto (%.2lf,%.2lf)\n", x1, y1);
    }
    else if ((y1 != y2) && (x1 == x2))
    {
        printf("Linea Vertical x=%0.2lf\n", x1);
    }
    else if ((y1 == y2) && (x1 != x2))
    {
        printf("Linea Horizontal y=%0.2lf\n", y1);
    }
    else if ((x1 < x2) && (y1 < y2))
    {
        printf("Recta Creciente y=%0.2lfx%+0.2lf\n", m, b);
    }
    else if ((x1 < x2) && (y1 > y2))
    {
        printf("Recta Decreciente y=%0.2lfx%+0.2lf\n", m, b);
    }

    return 0;
}
