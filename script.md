# Script
What side length would create an equilateral triangle with the same area and perimeter?
How about for other shapes, what side length would create a square with the same area and perimeter, what about a hexagon, or a pentagon?
There is one trivial solution for all these shapes, a side-length of zero,
but what about other, non-trivial solutions, does one even exist?

# The Triangle
To implore, let's start with a triangle.
<triangle>

We'll start by constructing our equation.
half-base times height = 3 * the side-length.

To find the area, we need the height.
Splitting the triangle down the middle turns the equilateral triangle into two right triangles.
We can now use the pythagorean theorem to find H.
In order to use the Pythagorean theorem, we need to know what to plug into it.
The hypotenuse's length is simply the equilateral triangle's side length, we'll call it S.
The bottom side of the right triangle is equal to half of S.
The side in the middle of the equilateral triangle is the height, H, which is what we need to find.
Now by substituting the values into the Pythagorean theorem,
we have an equation in terms of H and S.
We are left with two S squared variables, which we can simplify.
Then to find H we can take the square root of both sides of the equation.
Since the height is a length the plus or minus in the square root can be ignored.

## Solving the Original Problem
Now we are ready to solve the original problem we posed, what side length results in an equal area and perimeter for an equilateral triangle.

Substituting H in terms of S into the area formula for a triangle formula,
provides a formula for the area of an equilateral triangle.
This formula could be simplified further,
but the S's will be canceled in the next step.

The perimeter, is 3 times S.
Set these two equations equal, and cancel the common factors.

After simplifying the radical we are left with a final answer.
Using the formulas provides the same answer for both area and perimeter, this gives us the answer to our original question, a side length of 4 times the sqrt(3)
</triangle>

A similar method should work for other shapes.
Let's try adding a side, leading us to a square.
<square>
For a square the area is S squared,
and the perimeter is 4 times S.

This problem is very easy to solve, we simply set 4 * S equal to S^2 and divide both sides by s.
We end up with a solution s = 4.
</square>

Cool, so we've done this process for a triangle and a square...

I would say we'd try the pentagon next, but... the pentagon area formula is a bit...
Well, you can take a look for yourself.

For now, let's go on to the regular hexagon.
<hexagon>
A regular hexagon can be represented by six equilateral triangles and has an area of 6s^2 * sqrt(3) / 4

Perimeter has one S for every side, so for the hexagon, the perimter is 6s.
Set them equal, cancel the 6 and the S and then isolate the S and we have our solution, s = 4 / sqrt(3).
</hexagon>

So, we've found the sides for equilateral triangles, squares and regular hexagons that make the areas and perimeters of those corresponding shapes equal.

Now, let's ask a better question is there be a pattern? or will we have to find the side length manually each time?
The points of all regular polygons lie on a circle, so lets take this problem to its obvious limit, a circle.

<circle>
Instead of side length, radius will be used.
As is familiar by now, the area and perimeter formulas are used.
Set them equal, divide common factors, simplify, and solve.
A circle's perimeter equals its area when its radius equals 2.
</circle>

Instead of continuing on, with a heptagon, octagon, nonagon, and on,
maybe we should look for patterns, there must be regularities.

So, now with our understanding of the problems and what solving it looks like, let's try to solve for a general solution of any N-sided polygon.
Construct a regular polygon of N sides.
<general_triangle>
Lets take our ngon, and split it into triangles, as we can do.
The area of the n-gon is N times the area of one of its triangles.
The perimeter is N times the base of one triangle.
This means that the area and base of each triangle must be the same.
If the height of the triangle is two it will cancel with the two in the area formula,
leaving a result of b, the base.
This makes sense, considering how the circle had a radius of two.
Now we know that the height of the triangle is two, but how can that help us find b?
</general_triangle>
<trig>
Lets split our triangle in half, to get a right triangle.
After labeling what we know, the Pythagorean theorem won't help;
there are too many unknowns.
But we also know the angle, and trigonometry will help here,
the tangent function in particular.
The tangent of angle theta is the opposite side over the adjacent side.
Substituting our variables leads us to: tan theta equals b over 4.
Theta is half of the top angle of the triangle,
and there are N triangles making a full rotation, tau.
The angle theta is tau divided by two N.
Multiplying by 4 gives us the solution.
The side length is four times the tangent of tau divided by twice the number of sides.
</trig>
