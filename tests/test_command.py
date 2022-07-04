# -*- coding: utf-8 -*-

import os
import pytcm

def test_command_init():
    cmd = pytcm.Command('echo')

    assert cmd.binary == 'echo'
    assert cmd.opts == []
    assert cmd.cwd == os.getcwd()
    assert cmd.out is None
    assert cmd.err is None
    assert cmd.returncode is None

def test_command_opts_setter():
    cmd = pytcm.Command('echo')
    opt = pytcm.Flag('--verbose')
    cmd.opts = [opt]

    assert cmd.opts == [opt]
    assert cmd.opts[0].parse() == opt.parse()
