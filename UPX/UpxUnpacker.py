from x64dbgpy.pluginsdk import *
import sys

cip = register.GetCIP()
if memory.ReadByte(cip) != 0x60:
    gui.Message("Start at UPX entry point (1:[CIP]==0x60)")
    exit(0)

x64dbg.DbgCmdExecDirect("bc")
x64dbg.DbgCmdExecDirect("bphwc")
found = pattern.FindMem(cip, 0x1000, "83 EC ?? E9");
if found == 0:
    gui.Message("Could not find pattern!");
    exit(0)

debug.SetBreakpoint(found + 3)
debug.Run()
debug.StepIn()

cip = register.GetCIP()
comment.Set(cip, "OEP Found by Python!")
gui.Message("Reached OEP. Use Scylla to dump and restore imports!")
x64dbg.DbgCmdExec("scylla")
