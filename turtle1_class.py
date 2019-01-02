#! /usr/bin/env python

import turtle as t


class Draw(object):
    def __init__(self):
        self.diameter = 100
        self.gap = 10

        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0

        self.s1_x = self.start_x
        self.s1_y = self.start_y + (2 * self.diameter)
        self.e1_x = self.start_x
        self.e1_y = self.start_y + self.diameter

        self.s2_x = self.start_x + (2 * self.diameter)
        self.s2_y = self.start_y + (2 * self.diameter)
        self.e2_x = self.start_x + (2 * self.diameter)
        self.e2_y = self.start_y + self.diameter

        self.s3_x = self.start_x
        self.s3_y = self.start_y
        self.e3_x = self.start_x
        self.e3_y = self.start_y + self.diameter

        self.s4_x = self.start_x + (2 * self.diameter)
        self.s4_y = self.start_y
        self.e4_x = self.start_x + (2 * self.diameter)
        self.e4_y = self.start_y + (self.diameter)

        self.main()

    def draw_line(self, start_x, start_y, end_x, end_y):
        t.penup()
        t.goto(start_x, start_y)

        t.pendown()
        t.goto(end_x, end_y)

    def home(self):
        t.home()

    def done(self):
        t.done()

    def main(self):
        self.home()

        while self.s3_x <= (self.diameter - self.gap):

            self.draw_line(self.s1_x, self.s1_y, self.e1_x, self.e1_y)
            self.draw_line(self.s2_x, self.s2_y, self.e2_x, self.e2_y)
            self.draw_line(self.s3_x, self.s3_y, self.e3_x, self.e3_y)
            self.draw_line(self.s4_x, self.s4_y, self.e4_x, self.e4_y)

            self.s1_x =+ self.gap
            self.s1_y = self.s1_y
            self.e1_x = self.e1_x
            self.e1_y =+ self.gap

            self.s2_x =- self.gap
            self.s2_y = self.s2_y
            self.e2_x = self.e2_x
            self.e2_y =+ self.gap

            self.s3_x =+ self.gap
            self.s3_y = self.s3_y
            self.s3_x = self.s3_x
            self.e3_y =- self.gap

            self.s4_x =- self.gap
            self.s4_y = self.s4_y
            self.e4_x = self.e4_x
            self.e4_y =- self.gap

        self.done()

if __name__ == '__main__':

    Draw()

