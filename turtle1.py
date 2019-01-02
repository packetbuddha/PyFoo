#! /usr/bin/env python

import turtle as t

def draw_line(start_x, start_y, end_x, end_y):
	t.penup()
	t.goto(start_x, start_y)

	t.pendown()
	t.goto(end_x, end_y)


if __name__ == '__main__':
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0


    diameter = 100 
    gap = 10

    s1_x = start_x
    s1_y = start_y + (2 * diameter)
    e1_x = start_x
    e1_y = start_y + diameter

    s2_x = start_x + (2 * diameter)
    s2_y = start_y + (2 * diameter)
    e2_x = start_x + (2 * diameter)
    e2_y = start_y + diameter

    s3_x = start_x
    s3_y = start_y
    e3_x = start_x
    e3_y = start_y + diameter

    s4_x = start_x + (2 * diameter)
    s4_y = start_y
    e4_x = start_x + (2 * diameter)
    e4_y = start_y + (diameter)

    t.home()

    while s3_x <= (diameter - gap):

        draw_line(s1_x, s1_y, e1_x, e1_y)
        draw_line(s2_x, s2_y, e2_x, e2_y)
        draw_line(s3_x, s3_y, e3_x, e3_y)
        draw_line(s4_x, s4_y, e4_x, e4_y)

        s1_x = s1_x + gap
        #s1_y = s1_y
        #e1_x = e1_x
        e1_y = e1_y + gap

        s2_x = s2_x - gap
        #s2_y = s2_y
        #e2_x = e2_x
        e2_y = e2_y + gap

        s3_x = s3_x + gap
        #s3_y = s3_y
        #e3_x = e3_x
        e3_y = e3_y - gap

        s4_x = s4_x - gap
        #s4_y = s4_y
        #e4_x = e4_x
        e4_y = e4_y - gap

    t.done()
