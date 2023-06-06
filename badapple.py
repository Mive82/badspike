import hub
import os
import runtime


async def on_start(vm, stack):
    volume = 5
    vm.system.sound.volume(volume)
    vm.store.sound_volume(volume)
    file_size = os.stat("/frames")[6]
    n_frames = file_size // 25
    print(n_frames)
    badapple_file = open("/frames", "rb")
    vm.system.sound.play("/audio")
    b = badapple_file.read(25)
    slika = hub.Image(5, 5, b)
    time = vm.get_time()
    for _ in range(n_frames - 1):
        time = vm.get_time()
        vm.system.display.show(slika)
        b = badapple_file.read(25)
        slika = hub.Image(5, 5, b)
        while vm.get_time() < (time + 33):
            yield 0
    badapple_file.close()
    vm.stop()


def setup(rpc, system, stop):
    vm = runtime.VirtualMachine(rpc, system, stop, "something_unique")
    vm.register_on_start("another_unique_string", on_start)
    return vm
