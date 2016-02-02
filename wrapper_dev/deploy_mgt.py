#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os, curses, curses.ascii, subprocess
import glob
from time import sleep


class Wrapper(object):
    deploy_dir = os.path.join("..", "virtualisation", "autodeploy")

    def __init__(self, deploy_json):
        self.dir = os.path.dirname(deploy_json)
        self.name = os.path.basename(self.dir)
        self.zipname = self.name + ".zip"
        self.compress = False
        self.deployed = os.path.exists(os.path.join(Wrapper.deploy_dir, self.zipname))

    def __repr__(self):
        return "%s in %s will %s compress" % (self.name, self.dir, "" if self.compress else "not")

    def start_compress(self):
        log = open("log.txt", "a")

        filelist = os.listdir(self.dir)
        cmd = ["zip", "-r", os.path.join(os.path.dirname(self.dir), self.zipname)] + filelist
        log.write("executing " + " ".join(cmd) + " in " + self.dir)
        log.flush()
        proc = subprocess.Popen(cmd, cwd=self.dir, shell=False, stdout=log, stderr=log)
        proc.wait()

        cmd = ["mv", self.zipname, os.path.join(Wrapper.deploy_dir, self.zipname)]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.communicate()
        self.deployed = True

        log.close()

    def remove(self):
        if self.deployed:
            os.remove(os.path.join(Wrapper.deploy_dir, self.zipname))
            self.deployed = False


def get_root_dir():
    return os.path.dirname(os.path.abspath(__file__))


def find_wrapper():
    wrapper = []
    folders = glob.glob(os.path.join(get_root_dir(), "*/deploy.json"))
    for f in folders:
        wrapper.append(Wrapper(f))
    return wrapper


def draw_info(scr, wrapper):
    count_marked = len(filter(lambda x: x.compress, wrapper))
    scr.clear()
    scr.box()
    scr.addstr(1, 2, "Wrappers selected:")
    scr.addstr(1, 21, "%d/%d" % (count_marked, len(wrapper)))
    scr.addstr(2, 2, "Commands:")
    scr.addstr(2, 12, "Tab/Space/Enter = select; UP/DOWN = next/previous; r = undeploy;")
    scr.addstr(3, 12, "d = start deploying; n/p = scroll; ESC = exit")
    scr.refresh()


def draw_wrapper(scr, wrapper, start=0, current=0):
    height, width = scr.getmaxyx()
    end = min(len(wrapper), height - 2)  # minus box frame
    if end + start > len(wrapper):
        start = len(wrapper) - end
    scr.clear()
    scr.box()
    for i in range(0, end):
        w = wrapper[i + start]
        scr.addstr(i + 1, 1, "%s [%s] %s %s" % (
        ">" if i + start == current else " ", "X" if w.compress else " ", "D" if w.deployed else " ", w.name))
    scr.refresh()


def init_scr():
    scr = curses.initscr()
    height, width = scr.getmaxyx()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    control_height = 5
    chapter_list = curses.newwin(height - control_height, width, 0, 0)
    chapter_list.bkgd(curses.color_pair(1))

    control = curses.newwin(control_height, width, height - control_height, 0)
    control.keypad(1)
    control.bkgd(curses.color_pair(1))

    return control, chapter_list


def main():
    wrapper = find_wrapper()
    selected = 0

    scr, wrapper_list_win = init_scr()
    wrapper_list_start = 0

    while True:
        draw_info(scr, wrapper)
        draw_wrapper(wrapper_list_win, wrapper, wrapper_list_start, selected)
        curses.flushinp()
        c = scr.getch()

        if c == curses.ascii.ESC:
            break
        elif c == curses.ascii.SP or c == curses.ascii.NL or c == curses.ascii.TAB or c == curses.ascii.BS:
            wrapper[selected].compress = not wrapper[selected].compress

        elif c == curses.KEY_DOWN:
            if selected < len(wrapper) - 1:
                selected += 1

        elif c == curses.KEY_UP:
            if selected > 0:
                selected -= 1

        elif c == ord('n'):
            if wrapper_list_start <= len(wrapper):
                wrapper_list_start += 1

        elif c == ord('p'):
            if wrapper_list_start > 1:
                wrapper_list_start -= 1

        elif c == ord('d'):
            to_compress = filter(lambda x: x.compress, wrapper)
            to_compress_count = len(to_compress)
            counter = 0
            scr.addstr(1, 25, "deploying...")
            scr.refresh()
            for w in to_compress:
                w.start_compress()
                counter += 1
                scr.addstr(1, 25, "deployed: %d/%d" % (counter, to_compress_count))
                scr.refresh()
        elif c == ord('r'):
            wrapper[selected].remove()

    curses.endwin()

    return 0


if __name__ == '__main__':
    main()
