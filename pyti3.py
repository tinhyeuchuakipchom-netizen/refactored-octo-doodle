#!/bin/python3
# -*- coding: utf-8 -*-
if __import__('sys').version_info < (3, 9):raise MemoryError
try:
    import ast, random, base64, zlib, lzma, marshal, struct, time, sys, secrets, textwrap, os, uuid, unicodedata
    from ast import *
    from getpass import getpass
except:pass

text = """ ▄▄▄·▄▄▄         ▐▄▄▄▄▄▄ . ▄▄· ▄▄▄▄▄
▐█ ▄█▀▄ █·▪       ·██▀▄.▀·▐█ ▌▪•██
 ██▀·▐▀▀▄  ▄█▀▄ ▪▄ ██▐▀▀▪▄██ ▄▄ ▐█.▪  __OBF__: ProJect
▐█▪·•▐█•█▌▐█▌.▐▌▐▌▐█▌▐█▄▄▌▐███▌ ▐█▌·  __Author__: khangcoder X thảo my coder
.▀   .▀  ▀ ▀█▄▀▪ ▀▀▀• ▀▀▀ ·▀▀▀  ▀▀▀   __In4__: (https://www.facebook.com/profile.php?id=61593602324700)

"""
sys.setrecursionlimit(99999999)
ver = f"{sys.version_info.major}.{sys.version_info.minor}"

try:
    import textwrap
    from getpass import getpass
    from pystyle import *
except ModuleNotFoundError:
    print('>> Installing Module')
    __import__('os').system(f'{__import__("sys").executable} -m pip install pystyle --quiet')
    from pystyle import *

System.Clear()

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except: pass

def banner():
    try:
        a=Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), text)
        for i in range(len(a)):
            try:
                sys.stdout.write(a[i])
                sys.stdout.flush()
            except: pass
    except: pass
banner()

_used_var_names = set()

def _gen_unique_id(generator_func):
    for _ in range(10000):
        res = generator_func()
        if res not in _used_var_names:
            _used_var_names.add(res)
            return res
    res = f"Ox{uuid.uuid4().hex}"
    _used_var_names.add(res)
    return res

_hiragana_pool = [chr(i) for i in range(0x3041, 0x3097) if chr(i).isprintable() and chr(i).isidentifier()]
_katakana_pool = [chr(i) for i in range(0x30A1, 0x30FA) if chr(i).isprintable() and chr(i).isidentifier()]
_egyptian_pool = [chr(i) for i in range(0x13000, 0x13020) if chr(i).isprintable() and chr(i).isidentifier()]
_hangul_pool = [chr(i) for i in range(44032, 55204) if chr(i).isprintable() and chr(i).isidentifier()]

def rname():return _gen_unique_id(lambda: f"Ox{uuid.uuid4().hex[:7].upper()}")
def rb():return _gen_unique_id(lambda: ''.join(random.choices(_hiragana_pool, k=12)))
def rb1():return _gen_unique_id(lambda: f"Ox{uuid.uuid4().hex[:8].upper()}")
def rb2():return _gen_unique_id(lambda: ''.join(random.choices(_katakana_pool, k=12)))
def rb3():return _gen_unique_id(lambda: 'PyTi_Abi' + ''.join(random.choices(_egyptian_pool, k=5)))
def rb4():return _gen_unique_id(lambda: ''.join(random.choices(_hangul_pool, k=11)))
def rb5():return _gen_unique_id(lambda: ''.join(random.choices(_hangul_pool, k=8)))
def rbx():return ('decㅤcáiㅤlồnㅤmẹㅤmày'+''.join(random.choices("�?3�.�.4�thg = �c,2��a.ã.�45�$@dau = buoi�?3�.�.4��c,2��a.ã.�45�$@.2B.g .Bietㅤgiㅤveㅤbytecodeㅤkhong�?3�.�.4��c,2��a.ã.�45�$@chanbodicon�?3�.�.4��c,2��a.ã.�45�$@2g", k=1000))+''.join(random.choices([chr(i) for i in range(1000,3000) if chr(i).isprintable() and chr(i).isidentifier()], k=50))+'BỐㅤLÀㅤTRÙMㅤOBFㅤPYTIABI')
def superrandom():return ''.join(__import__('random').choices([chr(i) for i in range(1000, 3000)], k=600))
# DYNAMIC RANDOM OFFSETS (Fix Bug #9: eliminates static fingerprint constants)
_DYNAMIC_OFFSET_1 = secrets.randbits(58) + 10**16
_DYNAMIC_OFFSET_2 = secrets.randbits(60) + 10**17

# ============ PYTI HARDENING CORE (fix BUG #1/#2/#4/#5/#8/#18) ============
# Per-build random secrets: magic + stream constants + master keys.
# Every obfuscation run gets fresh values -> no static fingerprint to grep.
try:
    import hashlib as _hashlib_hard
except Exception:
    _hashlib_hard = None
_PYTI_SM_MAGIC = random.randint(0x1000, 0xFFFF)
_PYTI_SM_K1_MUL = random.choice([0x9E3779B9, 0x85EBCA6B, 0xC2B2AE35, 0x27D4EB2F, 0x165667B1, 0x1B873593])
_PYTI_SM_K1_ADD = random.randint(0x10000000, 0x7FFFFFFF)
_PYTI_SM_K2_MUL = random.choice([0xC2B2AE35, 0x9E3779B9, 0x85EBCA6B, 0x97E30D6D])
_PYTI_SM_K2_ADD = random.randint(0x10000000, 0x7FFFFFFF)
_PYTI_HVM_K = random.randint(0x10000000, 0x7FFFFFFF)
_PYTI_HVM_K2 = random.randint(0x10000000, 0x7FFFFFFF)
_PYTI_HVM_PEPPER = secrets.token_bytes(32)
_PYTI_HVM_WRAP_SALT = secrets.token_bytes(16)
_PYTI_HVM_EPOCH = random.choice((5, 6, 7, 8, 9, 10, 11, 12, 13))
_PYTI_HVM_UNWRAP_FN = '_hvmU'
_PYTI_URL_XOR = random.randint(1, 255)
_PYTI_URL_ROT = random.randint(1, 94)
_PYTI_BUILD_PEPPER = secrets.token_hex(16)
_PYTI_SM_SEED_SALT = secrets.token_hex(8)
_PYTI_INTEGRITY_SALT = random.randint(0x10000000, 0x7FFFFFFF)
_PYTI_HEARTBEAT_SECRET = random.randint(0x10000000, 0x7FFFFFFF)
_DEQUY_CACHE = {}


def _pyti_sha256(data: bytes) -> str:
    try:
        import hashlib as _h
        return _h.sha256(data).hexdigest()
    except Exception:
        # fallback: adler as hex (never empty)
        try:
            import zlib as _z
            return format(_z.adler32(data) & 0xFFFFFFFF, '08x') * 8
        except Exception:
            return '00' * 32


def _pyti_frag_bytes_expr(data: bytes, max_chunk: int = 48) -> str:
    """Return 'b\"\".join([...])' expr with random-sized chunks (no single blob)."""
    if not data:
        return "b''"
    parts = []
    i = 0
    min_chunk = max(8, max_chunk // 3) if max_chunk >= 24 else 8
    while i < len(data):
        n = random.randint(min_chunk, max_chunk)
        parts.append(repr(data[i:i + n]))
        i += n
    if len(parts) == 1:
        return parts[0]
    return 'b"".join([' + ','.join(parts) + '])'


def _pyti_chr_expr(s: str) -> str:
    """Hide a short ascii string as chr() arithmetic (anti-grep)."""
    if not s:
        return "''"
    k = random.randint(1, 32)
    elems = ','.join(f'(chr({ord(c) ^ k}^{k}))' for c in s)
    # join via empty chr-built string to avoid literal ''
    return f"''.join([{elems}])"


def _pyti_opaque_int(n: int) -> str:
    """Arithmetic/lambda expr that evaluates to n. Lambdas block const-fold."""
    n = int(n) & 0xFFFFFFFF
    a = random.randint(1, 0x7FFFFFFF)
    b = random.randint(1, 0x7FFF)
    mode = random.randint(0, 2)
    if mode == 0:
        return f'(lambda _a,_b:_a^_b)({n ^ a},{a})'
    if mode == 1:
        return f'(lambda _a,_b:(_a+_b)&0xFFFFFFFF)({(n - b) & 0xFFFFFFFF},{b})'
    return f'(lambda _a,_b:(_a-_b)&0xFFFFFFFF)({(n + a) & 0xFFFFFFFF},{a})'


def _pyti_opaque_bytes_expr(data: bytes) -> str:
    """Rebuild bytes from opaque uint32s. No bytes/b85 key blob in source."""
    if not data:
        return "b''"
    pad = (-len(data)) % 4
    raw = data + (b'\x00' * pad)
    chunks = []
    for i in range(0, len(raw), 4):
        n = int.from_bytes(raw[i:i + 4], 'big')
        chunks.append(f'({_pyti_opaque_int(n)}).to_bytes(4,"big")')
    joined = '+'.join(chunks)
    if pad:
        return f'({joined})[:{len(data)}]'
    return f'({joined})'


def _pyti_refresh_hvm_secrets():
    """Fresh rotating secrets per obfuscation run (never a static key in source)."""
    global _PYTI_HVM_K, _PYTI_HVM_K2, _PYTI_HVM_PEPPER, _PYTI_HVM_WRAP_SALT, _PYTI_HVM_EPOCH
    _PYTI_HVM_K = random.randint(0x10000000, 0x7FFFFFFF)
    _PYTI_HVM_K2 = random.randint(0x10000000, 0x7FFFFFFF)
    _PYTI_HVM_PEPPER = secrets.token_bytes(32)
    _PYTI_HVM_WRAP_SALT = secrets.token_bytes(16)
    _PYTI_HVM_EPOCH = random.choice((5, 6, 7, 8, 9, 10, 11, 12, 13))


def _pyti_hvm_epoch_block(seed, epoch_id, pepper: bytes, k_mul, k_add) -> bytes:
    hlib = _hashlib_hard
    if hlib is None:
        import hashlib as hlib
    h = hlib.sha256()
    h.update((int(seed) & 0xFFFFFFFFFFFFFFFF).to_bytes(8, 'big'))
    h.update((int(epoch_id) & 0xFFFFFFFF).to_bytes(4, 'big'))
    h.update(pepper)
    h.update((int(k_mul) & 0xFFFFFFFF).to_bytes(4, 'big'))
    h.update((int(k_add) & 0xFFFFFFFF).to_bytes(4, 'big'))
    return h.digest()


def _pyti_hvm_ins_keys(block: bytes, idx: int, num_ops: int):
    """Unique (k_op, k_arg) per instruction; material rotates every epoch."""
    w0 = int.from_bytes(block[0:4], 'big')
    w1 = int.from_bytes(block[4:8], 'big')
    w2 = int.from_bytes(block[8:12], 'big')
    w3 = int.from_bytes(block[12:16], 'big')
    w4 = int.from_bytes(block[16:20], 'big')
    w5 = int.from_bytes(block[20:24], 'big')
    w6 = int.from_bytes(block[24:28], 'big')
    mix = (w0 ^ (((idx + 1) * w1 + w2) & 0xFFFFFFFF)) & 0xFFFFFFFF
    mix2 = (w3 ^ (((idx + 3) * w4 + w2) & 0xFFFFFFFF)) & 0xFFFFFFFF
    mix = (mix ^ ((mix2 << 7) & 0xFFFFFFFF) ^ (mix2 >> 3)) & 0xFFFFFFFF
    k_op = (mix & 0xFF) % num_ops if num_ops else 0
    k_arg = (mix2 ^ ((((idx + 1) * w5) + w6) & 0xFFFFFFFF)) & 0xFFFFFFFF
    return k_op, k_arg


def _pyti_hvm_ctr_xor(data: bytes, pepper: bytes, salt: bytes) -> bytes:
    """SHA256-CTR wrap. Keystream block changes every 32 bytes — no stored XOR key."""
    hlib = _hashlib_hard
    if hlib is None:
        import hashlib as hlib
    out = bytearray(len(data))
    pos = 0
    ctr = 0
    while pos < len(data):
        blk = hlib.sha256(pepper + salt + ctr.to_bytes(4, 'big')).digest()
        n = min(32, len(data) - pos)
        for j in range(n):
            out[pos + j] = data[pos + j] ^ blk[j]
        pos += n
        ctr += 1
    return bytes(out)


def _pyti_b85_frag_expr(data: bytes) -> str:
    """b85 blob split into chunks joined at runtime."""
    try:
        import base64 as _b64
        txt = _b64.b85encode(data).decode('ascii')
    except Exception:
        txt = ''
    parts = []
    i = 0
    while i < len(txt):
        n = random.randint(32, 96)
        parts.append(repr(txt[i:i + n]))
        i += n
    if not parts:
        return "''"
    if len(parts) == 1:
        return parts[0]
    j = repr(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=4)))
    # opaque join order: ''.join(chunks)
    return '"".join([' + ','.join(parts) + '])'


def _compile_secure(src: str, filename: str = 'ProJect', mode: str = 'exec'):
    """Always reorder future-imports to top before compile (fix BUG #14)."""
    try:
        src = _fix_future_imports_src(src)
    except Exception:
        pass
    try:
        tree = ast.parse(src)
        try:
            tree = _fix_future_in_ast(tree)
        except Exception:
            pass
        ast.fix_missing_locations(tree)
        return compile(tree, filename, mode)
    except SyntaxError as _e:
        if 'from __future__' in str(_e):
            try:
                lines = src.splitlines()
                fut = [l for l in lines if l.strip().startswith('from __future__')]
                rest = [l for l in lines if not l.strip().startswith('from __future__')]
                return compile('\n'.join(fut + rest), filename, mode)
            except Exception:
                pass
        raise


def _protect_raw_payload(src: str, _depth_note: str = '') -> str:
    """Wrap a raw anti-hook/anti-debug payload so output holds only an
    encrypted fragmented blob + tiny polymorphic bootstrap (fix BUG #8).
    The blob is zlib+b85, split in chunks, decoded via indirect imports,
    verified by sha256 (fix BUG #18) before exec."""
    import base64 as _b64p, zlib as _zlp
    raw = src.encode('utf-8')
    digest = _pyti_sha256(raw)
    comp = _zlp.compress(raw, 9)
    b85expr = _pyti_b85_frag_expr(comp)
    v_blob = '_b' + uuid.uuid4().hex[:6]
    v_raw = '_r' + uuid.uuid4().hex[:6]
    v_dg = '_d' + uuid.uuid4().hex[:6]
    # indirect import names via chr() so 'import sys/os/ctypes' is not greppable
    imp_b64 = _pyti_chr_expr('base64')
    imp_zlib = _pyti_chr_expr('zlib')
    imp_hash = _pyti_chr_expr('hashlib')
    # split digest into 2 halves to avoid single hash literal
    h1, h2 = digest[:32], digest[32:]
    return (
        f"try:\n"
        f"    {v_blob}={b85expr}\n"
        f"    {v_raw}=__import__({imp_zlib}).decompress(__import__({imp_b64}).b85decode({v_blob}))\n"
        f"    {v_dg}=__import__({imp_hash}).sha256({v_raw}).hexdigest()\n"
        f"    assert {v_dg}==({h1!r}+{h2!r}),'integrity'\n"
        f"    exec({v_raw}.decode('utf-8'),globals(),globals())\n"
        f"except SystemExit:raise\n"
        f"except Exception:pass\n"
    )

def _unicodeobf(b):
    a = []
    for c in b:
        k = ord(c) + _DYNAMIC_OFFSET_1
        a.append(k)
    return a
def anhxa(b):
    return _unicodeobf(b)

def _unicodeobf1(b):
    a = []
    for c in b:
        k = ord(c) + _DYNAMIC_OFFSET_2
        a.append(k)
    return a
def anhxa1(b):
    return _unicodeobf1(b)

def wraphay(s, j='?3..4c,2a.ã.45$@.4__khangcoder_..12.44.124.6', ma=1):
    random.seed()
    __ok__ = []
    __vailon__ = []
    for c in s:
        sublist = []
        pos = len(sublist)
        sublist.append(c)
        for _ in range(random.randint(1, ma)):
            sublist.append(j)
        __ok__.append(sublist)
        __vailon__.append(pos)
    fmt = '%s' * len(s)
    args = ', '.join(f"{repr(sublist)}[{pos}]" for sublist, pos in zip(__ok__, __vailon__))
    return f"('{fmt}' % ({args}))"

def poison_code_object(co):
    # FIX BUG #10: randomized multi-traps + referenced dead-code + lineno mangling.
    # Old code appended ONE hardcoded unreferenced const (ignored by modern decompilers).
    # New: 2-3 randomized traps, dead LOAD_CONST reference via wrapper, random firstlineno.
    if not isinstance(co, types.CodeType):
        return co
    try:
        new_consts = []
        for c in co.co_consts:
            if isinstance(c, types.CodeType):
                new_consts.append(poison_code_object(c))
            else:
                new_consts.append(c)
        _variants = [
            'def _t_{r}():\n    try: pass\n    finally:\n        (lambda: (yield from (lambda: (yield 1))()))()\n',
            'async def _t_{r}():\n    try:\n        async with (lambda: __import__("contextlib").nullcontext())():\n            (lambda: [(yield i) for i in range(2)])()\n    finally:\n        pass\n',
            'def _t_{r}(_a=[(lambda: (yield from (lambda: (yield 1))()))()], _b={k!r}):\n    match _a:\n        case [_, *_]:\n            try:\n                with (lambda: __import__("contextlib").nullcontext())():\n                    pass\n            except* ValueError as _e:\n                pass\n    return (_b, _a)\n',
            'def _t_{r}():\n    _w = (_w0 := (_w1 := 0))\n    return [(_x := (lambda: (yield _x))()) for _x in range(1)]\n',
        ]
        for _vi in range(random.randint(2, 3)):
            _r = uuid.uuid4().hex[:6]
            _k = random.randint(1000, 9999)
            _src = random.choice(_variants).format(r=_r, k=_k)
            try:
                _trap = compile(_src, f'<__pyti_trap_{_r}__>', 'exec')
                # keep only inner function code objects to maximize decompiler load
                for _cc in list(getattr(_trap, 'co_consts', ())):
                    if isinstance(_cc, types.CodeType) and _cc.co_name.startswith('_t_'):
                        new_consts.append(_cc)
                        # also poison nested inside trap
                        break
                else:
                    new_consts.append(_trap)
            except Exception:
                continue
        # Mangle firstlineno (safe: only affects tracebacks) to break line-based decompilers
        _new_first = random.randint(10000, 90000)
        try:
            return co.replace(co_consts=tuple(new_consts), co_firstlineno=_new_first)
        except Exception:
            return co.replace(co_consts=tuple(new_consts))
    except Exception:
        return co


def gen_advanced_antipycdc():
    # FIX BUG #6: polymorphic bombs (random depths/counts) + hidden keywords (anti-grep).
    bombs = []

    # 1. Nested ternary expressions (Pycdc AST stack overflow) - random depth
    expr = '0'
    for _ in range(random.randint(5, 9)):
        r1, r2 = random.randint(1000, 9999), random.randint(1000, 9999)
        expr = f'({r1} if ({expr} == 0) else {r2})'
    bombs.append(f'_Ox_c_{random.randint(100,999)} = {expr}')

    # 2. Nested lambda chains - random depth
    lam_expr = 'lambda: 0'
    for i in range(random.randint(3, 6)):
        lam_expr = f'(lambda _x{i}_{uuid.uuid4().hex[:3]}: {lam_expr})'
    bombs.append(f'try:\n    _Ox_lam = {lam_expr}\nexcept: pass')

    # 3. Walrus operator nesting - random depth
    walrus = '0'
    for i in range(random.randint(3, 6)):
        walrus = f'(_w{i} := {walrus} + 1)'
    bombs.append(f'try:\n    _Ox_wal = {walrus}\nexcept: pass')

    # 4. Multi-level try-except-finally blocks - random depth
    for _ in range(random.randint(2, 3)):
        body = 'pass'
        for _ in range(random.randint(2, 3)):
            indented = textwrap.indent(body, '    ')
            _exc = random.sample(['TypeError', 'ValueError', 'RuntimeError', 'LookupError', 'ArithmeticError', 'OSError', 'KeyError'], k=random.randint(3, 5))
            body = f'try:\n{indented}\nexcept ({", ".join(_exc)}):\n    pass\nfinally:\n    int({random.randint(100,999)})'
        bombs.append(body)

    # 5. Recursive generator expression - randomized
    _rg_n = random.randint(2, 4)
    bombs.append(f'''try:
    _gen_bomb = [((lambda: [__x for __x in (lambda: (lambda: (yield from (lambda: (yield 1))()))())()])()) for _ in range({_rg_n})]
except: pass''')

    # 6. Function call chain - random depth
    antipycdc_calls = ''
    for _ in range(random.randint(10, 16)):
        antipycdc_calls += "decㅤcáiㅤlol(decㅤcáiㅤlol(decㅤcáiㅤlol(decㅤcáiㅤlol(decㅤcáiㅤlol(decㅤcáiㅤlol('  ')))))),"
    antipycdc_calls = 'try:khangcoder=[' + antipycdc_calls + ']\nexcept:pass'
    bombs.append(antipycdc_calls)
    # 7. NEW: deeply nested comprehension bomb (real parser load, not just AST junk)
    _comp_depth = random.randint(3, 5)
    _comp = '0'
    for _d in range(_comp_depth):
        _comp = f'[[{_comp} for _q{_d} in range(2)] for _p{_d} in range(2)]'
    bombs.append(f'try:\n    _Ox_comp_{random.randint(100,999)} = {_comp}\nexcept: pass')

    ast_bombs_str = '\n'.join(bombs)
    # Build hidden keyword blobs (anti-grep fix BUG #6/#7/#8)
    import base64 as _b64_ab
    _kw_ab = _b64_ab.b64encode(b'pycdc,decompyle,uncompyle,decompile,deobf,disassembl,pydisasm,unpyc,pyfluff,marshal_dump,tracer,hook_exec,hook_marshal,pylingual,pyarmor').decode()
    _pr_ab = _b64_ab.b64encode(b'pycdc,pycdc.exe,decompyle++,uncompyle6,decompyle,pydecomp,pylingual,xdis,pyarmor,pyfluff,decompile,unpyc,dis,pycdc_gui,ida.exe,ida64.exe,idag.exe,idaw.exe,x64dbg.exe,x32dbg.exe,x96dbg.exe,cheatengine.exe,scylla.exe,processhacker.exe,procmon.exe,wireshark.exe,fiddler.exe,charles.exe,httpcanary.exe,mitmproxy.exe,burpsuite.exe,dnspy.exe,de4dot.exe').decode()
    _md_ab = _b64_ab.b64encode(b'pycdc,decompyle,uncompyle,decompile,xdis,pydisasm,pylingual,deobfuscator').decode()
    
    active_engine = '''
_Ox1('-> Loading...', end='\\r')
j = []
if isinstance(j, (list, tuple, set, dict)):l = len(j)
def 你器你器(__chanbomaydi__):
    return __chanbomaydi__

# ==================== ADVANCED FULL ACTIVE ANTI-PYCDC ENGINE ====================
def __pyti_active_pycd_watchdog__():
    import sys, os, time
    import base64 as _b64w
    _bad_kw = tuple(_b64w.b64decode('__PYTI_KW_B64__').decode().split(','))
    _bad_procs = tuple(_b64w.b64decode('__PYTI_PR_B64__').decode().split(','))
    _bad_mods = tuple(_b64w.b64decode('__PYTI_MD_B64__').decode().split(','))
    def _kill_procs():
        try:
            import ctypes
            # Bug #6 Fix: Check window titles so renaming x64dbg.exe -> abc.exe is detected
            _u32 = getattr(getattr(ctypes, 'windll', None), 'user32', None)
            if _u32 and hasattr(_u32, 'GetWindowTextW') and hasattr(_u32, 'EnumWindows'):
                _bad_titles = ('x64dbg', 'x32dbg', 'ida pro', 'ida -', 'cheat engine', 'process hacker', 'wireshark', 'fiddler', 'http debugger')
                @ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)
                def _w_enum_cb(hwnd, lparam):
                    if _u32.IsWindowVisible(hwnd):
                        buf = ctypes.create_unicode_buffer(512)
                        _u32.GetWindowTextW(hwnd, buf, 512)
                        val = buf.value.lower()
                        if any(t in val for t in _bad_titles):
                            os._exit(138)
                    return True
                _u32.EnumWindows(_w_enum_cb, 0)
        except Exception: pass
        try:
            import ctypes
            TH32CS_SNAPPROCESS = 0x00000002
            PROCESS_TERMINATE = 0x0001
            _windll = getattr(ctypes, 'windll', None)
            k32 = None
            if _windll is not None:
                try:
                    k32 = _windll.kernel32
                except Exception:
                    k32 = None
            if k32 is not None:
                class PROCESSENTRY32W(ctypes.Structure):
                    _fields_ = [
                        ('dwSize', ctypes.c_ulong), ('cntUsage', ctypes.c_ulong),
                        ('th32ProcessID', ctypes.c_ulong), ('th32DefaultHeapID', ctypes.c_size_t),
                        ('th32ModuleID', ctypes.c_ulong), ('cntThreads', ctypes.c_ulong),
                        ('th32ParentProcessID', ctypes.c_ulong), ('pcPriClassBase', ctypes.c_long),
                        ('dwFlags', ctypes.c_ulong), ('szExeFile', ctypes.c_wchar * 260)
                    ]
                hSnap = k32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
                if hSnap != -1:
                    pe = PROCESSENTRY32W()
                    pe.dwSize = ctypes.sizeof(PROCESSENTRY32W)
                    if k32.Process32FirstW(hSnap, ctypes.byref(pe)):
                        while True:
                            exe = pe.szExeFile.lower()
                            if any(x in exe for x in _bad_procs):
                                hProc = k32.OpenProcess(PROCESS_TERMINATE, False, pe.th32ProcessID)
                                if hProc:
                                    k32.TerminateProcess(hProc, 1)
                                    k32.CloseHandle(hProc)
                                os._exit(137)
                            if not k32.Process32NextW(hSnap, ctypes.byref(pe)): break
                    k32.CloseHandle(hSnap)
        except Exception: pass
        try:
            if os.path.exists('/proc'):
                for e in os.listdir('/proc'):
                    if e.isdigit():
                        try:
                            with open(f'/proc/{e}/cmdline', 'rb') as f:
                                c = f.read().decode('latin1', 'ignore').lower()
                                if any(x in c for x in _bad_procs):
                                    try: os.kill(int(e), 9)
                                    except: pass
                                    os._exit(137)
                        except: pass
        except Exception: pass

    def _hard_die(code=95):
        try:
            import ctypes as _cd
            _k = getattr(getattr(_cd, 'windll', None), 'kernel32', None)
            if _k and hasattr(_k, 'TerminateProcess'): _k.TerminateProcess(_k.GetCurrentProcess(), 0xC0000005)
            _nt = getattr(getattr(_cd, 'windll', None), 'ntdll', None)
            if _nt and hasattr(_nt, 'NtTerminateProcess'): _nt.NtTerminateProcess(-1, 0xC0000005)
            _cd.memset(0, 0, 1)
        except: pass
        try: os.abort()
        except: pass
        os._exit(code)

    _pulse_cnt = 0
    while True:
        try:
            _pulse_cnt = (_pulse_cnt + 1) & 0xFFFFFFFF
            try:
                import sys as _sw, time as _tw
                _g = getattr(_sw.modules.get('__main__'), '__dict__', None) or globals()
                _g['__pyti_pulse__'] = (_tw.time(), (_pulse_cnt ^ 0x5F3759DF))
            except Exception: pass
            if sys.gettrace() is not None: _hard_die(95)
            if hasattr(sys, 'monitoring'):
                for _ti in range(6):
                    _ev = sys.monitoring.get_events(_ti)
                    _tl = sys.monitoring.get_tool(_ti)
                    if _ev != 0 or (_tl is not None and not str(_tl).startswith('pyti_')):
                        _hard_die(95)
            for f in sys._current_frames().values():
                cf = f
                while cf:
                    co_fn = (getattr(cf.f_code, 'co_filename', '') or '').lower()
                    fn_name = (getattr(cf.f_code, 'co_name', '') or '').lower()
                    if any(x in co_fn or x in fn_name for x in _bad_kw):
                        _hard_die(97)
                    cf = cf.f_back
            for m in list(sys.modules.keys()):
                if any(x in m.lower() for x in _bad_mods):
                    _hard_die(96)
            # Full 24-byte hook pattern coverage
            try:
                import ctypes
                try: _pyapi = object.__getattribute__(ctypes, 'pythonapi')
                except Exception: _pyapi = getattr(ctypes, 'pythonapi', None)
                for sym in ('PyMarshal_ReadObjectFromString', 'PyEval_EvalCode', '_PyEval_EvalFrameDefault', 'PyRun_StringFlags', 'PyObject_Call'):
                    try: addr = getattr(_pyapi, sym, None)
                    except Exception: continue
                    if addr:
                        ptr = ctypes.cast(addr, ctypes.c_void_p).value
                        if ptr:
                            b = bytes((ctypes.c_ubyte * 24).from_address(ptr))
                            if (b[0] in (0xE9, 0xEB, 0xCC, 0xC3, 0xC2)
                                or (b[0] == 0xFF and len(b) > 1 and b[1] in (0x25, 0xE0, 0xE1, 0xE2))
                                or (b[0] == 0x48 and len(b) > 1 and b[1] == 0xB8)
                                or (b[0] == 0xCD and len(b) > 1 and b[1] == 0x03)
                                or (b[0] == 0xB8 and len(b) > 6 and b[5] == 0xFF and b[6] == 0xE0)
                                or (b[0] == 0x68 and len(b) > 5 and b[5] == 0xC3)
                                or (len(b) >= 3 and b[0] == 0x90 and b[1] == 0x90 and b[2] == 0x90)):
                                _hard_die(91)
                            for off in (1, 2, 3):
                                if len(b) > off + 2 and (b[off] in (0xE9, 0xCC) or (b[off] == 0xFF and b[off+1] == 0x25) or (b[off] == 0x48 and b[off+1] == 0xB8)):
                                    _hard_die(91)
            except Exception: pass
            _kill_procs()
        except Exception: pass
        time.sleep(1.0)

try:
    if '__pyti_watchdog_active__' not in globals():
        globals()['__pyti_watchdog_active__'] = True
        try:
            import _thread as _th_act
            _th_act.start_new_thread(__pyti_active_pycd_watchdog__, ())
        except Exception:
            import threading as _th_act
            _th_act.Thread(target=__pyti_active_pycd_watchdog__, daemon=True).start()
except Exception: pass
'''
    try:
        active_engine = active_engine.replace('__PYTI_KW_B64__', _kw_ab).replace('__PYTI_PR_B64__', _pr_ab).replace('__PYTI_MD_B64__', _md_ab)
    except Exception:
        pass
    return active_engine + '\n' + ast_bombs_str + '\nfinally:int(2009-1711)\n'

ANTI_PYCDC = gen_advanced_antipycdc()

trap = rb()
trap1 = rb2()
# --- ENCODE LAYERS VĨNH VIỄN ---
def _enc_a(s): return wraphay(s)
def _enc_b(s): return wraphay(''.join(str(ord(c)+_DYNAMIC_OFFSET_1) for c in s))
def _enc_c(s):
    _daubuoi = "0123456789"
    _ancut = "ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ"
    _trash = dict(zip(_daubuoi, _ancut))
    t = ''.join(str(b).zfill(3) for b in s.encode())
    p = ''.join(_trash.get(c, c) for c in t)
    return f"__pyti_enc3__({repr(p)})"
def _enc_d(s):
    import base64, zlib
    return base64.b64encode(zlib.compress(s.encode(), 9)).decode()
# --- ANTI DEBUG / ANTI HOOK / ANTI REQUEST HOOK ---
import types, inspect, time, os, builtins

_X1 = rb(); _X2 = rb1(); _X3 = rb4()

_FDBG = rb(); _FDBG2 = rb()

# --- FIXED FULL POWER ANTI DEBUG (generator self-protection) ---
_FDBG_CODE = f"""
def {_FDBG}(b=None):
    import sys, os, time, platform, builtins, types
    # 1. basic debugger detection (Bug #3 fix: do not swallow SystemExit)
    try:
        if sys.gettrace() is not None:
            raise SystemExit('DEBUG_GETTRACE')
    except SystemExit: raise
    except Exception: pass
    try:
        if hasattr(sys, 'getprofile') and sys.getprofile() is not None:
            raise SystemExit('DEBUG_GETPROFILE')
    except SystemExit: raise
    except Exception: pass
    try:
        if getattr(sys.flags, 'debug', 0) != 0:
            raise SystemExit('DEBUG_FLAG')
    except SystemExit: raise
    except Exception: pass
    try:
        if hasattr(sys, 'monitoring'):
            for _ti in range(6):
                _ev = sys.monitoring.get_events(_ti)
                _tl = sys.monitoring.get_tool(_ti)
                if _ev != 0 or (_tl is not None and not str(_tl).startswith('pyti_')):
                    raise SystemExit('PEP669_MONITORING')
            for _ti in range(6):
                try: sys.monitoring.use_tool_id(_ti, 'pyti_' + str(_ti))
                except: pass
                try: sys.monitoring.set_events(_ti, 0)
                except: pass
    except SystemExit: raise
    except Exception: pass
    try:
        if getattr(builtins, '__IPYTHON__', None) is not None:
            raise SystemExit('IPYTHON')
    except SystemExit: raise
    except Exception: pass
    # env vars
    try:
        _bad_env = ('PYTHONDEBUG','PYTHONBREAKPOINT','PYDEVD_LOAD_VALUES_ASYNC','PYCHARM','VSCODE_PID','TERM_PROGRAM')
        for _k in _bad_env:
            if os.environ.get(_k):
                raise SystemExit('ENV_DEBUG_' + _k)
        if os.environ.get('PDB') or os.environ.get('DEBUG'):
            raise SystemExit('ENV_DEBUG')
    except SystemExit: raise
    except Exception: pass
    # sys.modules debugger modules
    try:
        _dbg_mods = ('pdb','bdb','pydevd','debugpy','ptvsd','cProfile','pycdc','decompyle','uncompyle','xdis','pyfluff','pylingual')
        for _m in list(sys.modules.keys()):
            _ml = _m.lower()
            if any(x in _ml for x in _dbg_mods):
                raise SystemExit('MODULE_DEBUG_' + _m)
    except SystemExit: raise
    except Exception: pass
    # timing anti-hook / anti-emu (Bug #4 fix: calibrate baseline first to avoid slow VPS false positives)
    try:
        _t_cal0 = time.perf_counter()
        for _i in range(1000): pass
        _t_base = max(time.perf_counter() - _t_cal0, 1e-6)
        _t0 = time.perf_counter()
        _s = 0
        for _i in range(10000):
            _s += _i
        if (time.perf_counter() - _t0) > max(_t_base * 40, 3.5):
            raise SystemExit('TIMING_HOOK')
    except SystemExit: raise
    except Exception: pass
    # Real hypervisor / sandbox detection (firmware + services + DMI, not env-only fake checks)
    try:
        if os.environ.get('PYTI_ALLOW_VM') == '1':
            pass
        else:
            _vm_score = 0
            _vm_tok = ('vmware','virtualbox','qemu','sandbox','kvm','xen','vbox','bochs','innotek','parallels','hyper-v','virtual machine','tcg')
            try:
                if os.environ.get('WINELOADER') or os.environ.get('WINEPREFIX'):
                    _vm_score += 2
            except: pass
            try:
                _node = (platform.node() or '').lower()
                if any(x in _node for x in _vm_tok):
                    _vm_score += 1
            except: pass
            try:
                import uuid
                _mac = f"{{uuid.getnode():012x}}".lower()
                if _mac[:6] in ('000569','000c29','001c14','005056','080027','525400','001c42','0003ff'):
                    _vm_score += 1
            except: pass
            try:
                if os.name == 'nt':
                    import winreg
                    try:
                        _k = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\\\\DESCRIPTION\\\\System\\\\BIOS")
                        _mfg = str(winreg.QueryValueEx(_k, "SystemManufacturer")[0]).lower()
                        _prod = str(winreg.QueryValueEx(_k, "SystemProductName")[0]).lower()
                        winreg.CloseKey(_k)
                        if any(x in _mfg or x in _prod for x in _vm_tok) or ('virtual' in _prod):
                            _vm_score += 2
                    except OSError:
                        pass
                    for _rk in (r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\VBoxGuest', r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\VBoxMouse', r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\VMTools', r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\vmmouse', r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\vmci', r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\xeniface', r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\balloon'):
                        try:
                            _sk = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, _rk)
                            winreg.CloseKey(_sk)
                            _vm_score += 2
                            break
                        except OSError:
                            pass
                    try:
                        import ctypes as _ctv
                        _k32 = getattr(getattr(_ctv, 'windll', None), 'kernel32', None)
                        if _k32 and hasattr(_k32, 'GetSystemFirmwareTable'):
                            _n = _k32.GetSystemFirmwareTable(0x52534D42, 0, None, 0)
                            if _n:
                                _buf = (_ctv.c_char * _n)()
                                _k32.GetSystemFirmwareTable(0x52534D42, 0, _buf, _n)
                                _sm = bytes(_buf).lower()
                                for _tok in (b'vmware', b'virtualbox', b'qemu', b'vbox', b'bochs', b'xen', b'kvm', b'hyper-v', b'tcg', b'parallels', b'innotek', b'virtual machine', b'virtual hd'):
                                    if _tok in _sm:
                                        _vm_score += 2
                                        break
                    except Exception:
                        pass
            except: pass
            try:
                if os.name == 'nt':
                    _v_drv = (r'C:\\\\Windows\\\\System32\\\\drivers\\\\VBoxMouse.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\VBoxGuest.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\VBoxSF.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\vmmouse.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\vmci.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\vmxnet.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\vmmemctl.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\balloon.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\netkvm.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\vioscsi.sys')
                    if any(os.path.exists(_d) for _d in _v_drv):
                        _vm_score += 2
            except: pass
            try:
                for _p in ('/sys/class/dmi/id/product_name', '/sys/class/dmi/id/sys_vendor', '/sys/class/dmi/id/bios_vendor', '/sys/hypervisor/type'):
                    if os.path.exists(_p):
                        with open(_p, 'r', errors='ignore') as _df:
                            _dv = _df.read().lower()
                        if any(x in _dv for x in _vm_tok):
                            _vm_score += 2
                            break
            except: pass
            try:
                if os.path.exists('/proc/cpuinfo'):
                    with open('/proc/cpuinfo', 'r', errors='ignore') as _cf:
                        _ci = _cf.read().lower()
                    if 'hypervisor' in _ci:
                        _vm_score += 1
            except: pass
            if _vm_score >= 2:
                raise SystemExit('VM_DETECTED')
    except SystemExit: raise
    except Exception: pass
    # builtins integrity - FIX BUG #13: identity + isbuiltin (no str(type) spoof, no PyPy false-positive)
    try:
        import types as _t_bi
        _BuiltinTypes = getattr(_t_bi, 'BuiltinFunctionType', type(len)), getattr(_t_bi, 'BuiltinMethodType', type(len))
        try:
            if builtins.__dict__.get('open', open) is not open:
                raise SystemExit('HOOK_OPEN')
        except SystemExit: raise
        except Exception: pass
        for _bn in ('print','compile','eval','exec','__import__'):
            try:
                _obj = getattr(builtins, _bn, None)
                if _obj is None: continue
                # 1) identity must match builtins dict
                try:
                    if builtins.__dict__.get(_bn) is not _obj:
                        raise SystemExit('HOOK_BUILTIN_' + _bn.upper())
                except SystemExit: raise
                except Exception: pass
                # 2) must be real builtin type (blocks python-level wrappers with fake __module__)
                if not isinstance(_obj, _BuiltinTypes):
                    # allow only if __self__ is builtins module (bound builtin)
                    if getattr(_obj, '__self__', None) is not builtins:
                        if getattr(_obj, '__module__', '') not in ('builtins','_builtins','__builtin__'):
                            raise SystemExit('HOOK_BUILTIN_' + _bn.upper())
                        # wrapper with fake module but not builtin type -> still hook
                        raise SystemExit('HOOK_BUILTIN_' + _bn.upper())
            except SystemExit: raise
            except Exception: continue
    except SystemExit: raise
    except: pass
    # IsDebuggerPresent & Window Detection (Windows - Bug #6 Fix)
    try:
        import ctypes
        _wd = getattr(ctypes, 'windll', None)
        if _wd is not None:
            try:
                _u32 = getattr(_wd, 'user32', None)
                if _u32 and hasattr(_u32, 'GetWindowTextW') and hasattr(_u32, 'EnumWindows'):
                    _dtitles = ('x64dbg', 'x32dbg', 'ida pro', 'ida -', 'cheat engine', 'process hacker', 'wireshark', 'fiddler')
                    @ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)
                    def _ew_cb(hwnd, lp):
                        if _u32.IsWindowVisible(hwnd):
                            buf = ctypes.create_unicode_buffer(512)
                            _u32.GetWindowTextW(hwnd, buf, 512)
                            val = buf.value.lower()
                            if any(t in val for t in _dtitles):
                                raise SystemExit('DEBUGGER_WINDOW')
                        return True
                    _u32.EnumWindows(_ew_cb, 0)
            except SystemExit: raise
            except: pass
            try:
                _k = _wd.kernel32
                if _k.IsDebuggerPresent():
                    raise SystemExit('WIN_DEBUGGER')
                _is_remote = ctypes.c_bool(False)
                _k.CheckRemoteDebuggerPresent(_k.GetCurrentProcess(), ctypes.byref(_is_remote))
                if _is_remote.value:
                    raise SystemExit('WIN_REMOTE_DEBUGGER')
                # NtQueryInformationProcess & ThreadHideFromDebugger
                try:
                    _ntdll = _wd.ntdll
                    _ph = _k.GetCurrentProcess()
                    try: _ntdll.NtSetInformationThread(_k.GetCurrentThread(), 0x11, 0, 0)
                    except: pass
                    _dbg_port = ctypes.c_ulong(0)
                    _status = _ntdll.NtQueryInformationProcess(_ph, 7, ctypes.byref(_dbg_port), ctypes.sizeof(_dbg_port), None)
                    if _status == 0 and _dbg_port.value != 0:
                        raise SystemExit('NT_DEBUG_PORT')
                    _dbg_flags = ctypes.c_ulong(1)
                    _status = _ntdll.NtQueryInformationProcess(_ph, 0x1F, ctypes.byref(_dbg_flags), ctypes.sizeof(_dbg_flags), None)
                    if _status == 0 and _dbg_flags.value == 0:
                        raise SystemExit('NT_DEBUG_FLAGS')
                except: pass
            except SystemExit: raise
            except: pass
    except: pass
    # ptrace anti-debug on Linux (TracersPid)
    try:
        if os.path.exists('/proc/self/status'):
            with open('/proc/self/status','r',errors='ignore') as _f:
                for _line in _f:
                    if _line.startswith('TracerPid:'):
                        _pid = _line.split(':',1)[1].strip()
                        if _pid != '0':
                            raise SystemExit('PTRACE_DETECTED')
                        break
    except SystemExit: raise
    except: pass
    # open file hook check
    try:
        _orig_open = open
        if open is not builtins.open:
            raise SystemExit('HOOK_OPEN2')
    except: pass
"""
exec(_FDBG_CODE)


_A = rb(); _B = rb1(); _C = rb2()
exec(f"{_FDBG}()")

# bảo vệ hook code
_A2 = rb(); _A3 = rb1()
_FHOOK = rb()
# FIXED _FHOOK with proper reference guard
exec(f"def {_FHOOK}(obj, nm):\n"
     f"    _is_d = isinstance(obj, dict)\n"
     f"    orig = obj.get(nm, None) if _is_d else getattr(obj, nm, None)\n"
     f"    if orig is None or not callable(orig): return\n"
     f"    _ref = [None]\n"
     f"    def guard(*a, **kw):\n"
     f"        cur = obj.get(nm, None) if _is_d else getattr(obj, nm, None)\n"
     f"        if cur is not _ref[0]:\n"
     f"            raise SystemExit('HOOK_DETECTED_' + str(nm).upper())\n"
     f"        return orig(*a, **kw)\n"
     f"    _ref[0] = guard\n"
     f"    try:\n"
     f"        guard.__wrapped__ = orig\n"
     f"    except Exception: pass\n"
     f"    try:\n"
     f"        if _is_d: obj[nm] = guard\n"
     f"        else: setattr(obj, nm, guard)\n"
     f"    except Exception: pass\n")

# --- FIXED HOOK PROTECTION (Bug #11 Fix: protect builtins whether dict or ModuleType) ---
try:
    _hook_targets = [
        (sys, ('stdout','stderr','stdin','modules','exit')),
        (builtins, ('exit','quit','input','open','compile','eval','exec','__import__','print')),
    ]
    if isinstance(__builtins__, dict):
        _hook_targets.append((__builtins__, ('exit','quit','input','open','compile','eval','exec','__import__','print')))
    for _t, _names in _hook_targets:
        for _n in _names:
            try:
                _FHOOK(_t, _n)
            except Exception:
                pass
except Exception:
    pass

# chống hook requests / urllib
# --- FIXED urllib.request PROTECTION ---
try:
    _ur = __import__('urllib.request', fromlist=['urlopen'])
    _o = getattr(_ur, 'urlopen', None)
    if callable(_o):
        _ur_original_urlopen = _o
        def _hurl(*a, **kw):
            cur = getattr(_ur, 'urlopen', None)
            # check if hook replaced our wrapper
            if cur is not _hurl:
                # if someone replaced after us, cur != _hurl -> hook detected
                # but we allow only our wrapper, otherwise exit
                if cur is not _ur_original_urlopen and cur is not _hurl:
                    raise SystemExit('REQUEST_HOOK_URLLIB')
            return _ur_original_urlopen(*a, **kw)
        _ur.urlopen = _hurl
        # also protect OpenerDirector
        try:
            _OD = getattr(_ur, 'OpenerDirector', None)
            if _OD and hasattr(_OD, 'open'):
                _orig_OD_open = _OD.open
                _guard_ref = [None]
                def _od_guard(self, *a, **kw):
                    if getattr(_OD, 'open', None) is not _guard_ref[0]:
                        raise SystemExit('HOOK_OPENER')
                    return _orig_OD_open(self, *a, **kw)
                _guard_ref[0] = _od_guard
                _OD.open = _od_guard
        except Exception:
            pass
except Exception:
    pass

# --- FIXED requests API PROTECTION ---
try:
    _rq = __import__('requests')
    for _rn in ('get','post','put','delete','request','patch','head','options'):
        try:
            orig = getattr(_rq, _rn, None)
            if not callable(orig):
                continue
            # need closure to capture orig and name correctly
            def _make_rguard(_orig, _name):
                _ref = [None]
                def _wrap(*a, **kw):
                    if getattr(_rq, _name, None) is not _ref[0]:
                        raise SystemExit('REQUEST_HOOK_' + _name.upper())
                    return _orig(*a, **kw)
                _ref[0] = _wrap
                # preserve metadata
                try:
                    _wrap.__name__ = getattr(_orig, '__name__', _name)
                    _wrap.__wrapped__ = _orig
                except: pass
                return _wrap
            setattr(_rq, _rn, _make_rguard(orig, _rn))
        except Exception:
            pass
    # protect Session.request separately with stronger guard
    try:
        import requests.sessions
        _Sess = requests.sessions.Session
        _orig_sess_req = getattr(_Sess, 'request', None)
        if callable(_orig_sess_req):
            _sess_ref = [None]
            def _sess_guard(self, *a, **kw):
                if getattr(_Sess, 'request', None) is not _sess_ref[0]:
                    raise SystemExit('HOOK_SESSION_REQUEST')
                return _orig_sess_req(self, *a, **kw)
            _sess_ref[0] = _sess_guard
            _Sess.request = _sess_guard
    except Exception:
        pass
except Exception:
    pass

# --- NANG CAP FULL POWER ANTI HOOK (FIXED) ---
try:
    import urllib3.connectionpool as _u_pool_mod
    import urllib.request as _u_req_mod
    import http.client as _http_mod
    import requests.adapters as _req_adapt_mod
    import requests.api as _req_api_mod
    import requests as _req_mod

    # 1) urllib3 HTTPConnectionPool.urlopen
    try:
        _Pool = _u_pool_mod.HTTPConnectionPool
        _orig_pool_urlopen = getattr(_Pool, 'urlopen', None)
        if callable(_orig_pool_urlopen):
            _pool_ref = [None]
            def _pool_urlopen_guard(self, *a, **kw):
                if getattr(_Pool, 'urlopen', None) is not _pool_ref[0]:
                    raise SystemExit('REQUEST_HOOK_POOL')
                return _orig_pool_urlopen(self, *a, **kw)
            _pool_ref[0] = _pool_urlopen_guard
            _Pool.urlopen = _pool_urlopen_guard
    except Exception: pass

    # 2) http.client HTTPConnection methods
    try:
        _HC = _http_mod.HTTPConnection
        for _mname in ('request','putrequest','getresponse','endheaders','send'):
            try:
                _orig_m = getattr(_HC, _mname, None)
                if not callable(_orig_m): continue
                def _make_http_guard(_orig, _name):
                    _ref = [None]
                    def _guard(self, *a, **kw):
                        if getattr(_HC, _name, None) is not _ref[0]:
                            raise SystemExit('HOOK_HTTP_' + _name.upper())
                        return _orig(self, *a, **kw)
                    _ref[0] = _guard
                    return _guard
                setattr(_HC, _mname, _make_http_guard(_orig_m, _mname))
            except Exception: continue
        # also HTTPSConnection
        try:
            _HCS = getattr(_http_mod, 'HTTPSConnection', None)
            if _HCS:
                for _mname in ('request','putrequest'):
                    try:
                        _orig_m = getattr(_HCS, _mname, None)
                        if not callable(_orig_m): continue
                        def _make_https_guard(_orig, _name):
                            _ref = [None]
                            def _guard(self, *a, **kw):
                                if getattr(_HCS, _name, None) is not _ref[0]:
                                    raise SystemExit('HOOK_HTTPS_' + _name.upper())
                                return _orig(self, *a, **kw)
                            _ref[0] = _guard
                            return _guard
                        setattr(_HCS, _mname, _make_https_guard(_orig_m, _mname))
                    except: continue
        except: pass
    except Exception: pass

    # 3) requests.adapters HTTPAdapter.send
    try:
        _Adp = _req_adapt_mod.HTTPAdapter
        _orig_adp_send = getattr(_Adp, 'send', None)
        if callable(_orig_adp_send):
            _adp_ref = [None]
            def _guard_adapter_send(self, *a, **kw):
                if getattr(_Adp, 'send', None) is not _adp_ref[0]:
                    raise SystemExit('HOOK_ADAPTER_SEND')
                return _orig_adp_send(self, *a, **kw)
            _adp_ref[0] = _guard_adapter_send
            _Adp.send = _guard_adapter_send
    except Exception: pass

    # 4) requests.api functions
    try:
        for _fn in ('request','get','post','put','delete','patch','head','options'):
            try:
                _orig = getattr(_req_api_mod, _fn, None)
                if not callable(_orig): continue
                def _make_api_guard(_orig, _name):
                    _ref = [None]
                    def _wrap(*a, **kw):
                        if getattr(_req_api_mod, _name, None) is not _ref[0]:
                            raise SystemExit('HOOK_API_' + _name.upper())
                        return _orig(*a, **kw)
                    _ref[0] = _wrap
                    return _wrap
                setattr(_req_api_mod, _fn, _make_api_guard(_orig, _fn))
            except: continue
    except Exception: pass

    # 5) builtins.__import__ guard - DISABLED for generator to avoid self-lock (payload has separate protection)
    try:
        pass
    except Exception:
        pass

    # 6) inspect.getmembers guard
    try:
        import inspect as _ins_mod
        if hasattr(_ins_mod, 'getmembers'):
            _orig_gm = _ins_mod.getmembers
            if callable(_orig_gm):
                _gm_ref = [None]
                def _guard_getmembers(obj, *a, **kw):
                    if getattr(_ins_mod, 'getmembers', None) is not _gm_ref[0]:
                        raise SystemExit('HOOK_INSPECT_GETMEMBERS')
                    return _orig_gm(obj, *a, **kw)
                _gm_ref[0] = _guard_getmembers
                _ins_mod.getmembers = _guard_getmembers
    except Exception: pass

    # 7) socket.getaddrinfo / gethostbyname / socket.send + enhanced socket.socket + ssl
    try:
        import socket as _sock_mod
        for _sname in ('getaddrinfo','gethostbyname','gethostbyname_ex','create_connection','getfqdn'):
            try:
                _orig = getattr(_sock_mod, _sname, None)
                if not callable(_orig): continue
                def _make_sock_guard(_orig, _name):
                    _ref = [None]
                    def _wrap(*a, **kw):
                        if getattr(_sock_mod, _name, None) is not _ref[0]:
                            raise SystemExit('HOOK_SOCKET_' + _name.upper())
                        return _orig(*a, **kw)
                    _ref[0] = _wrap
                    return _wrap
                setattr(_sock_mod, _sname, _make_sock_guard(_orig, _sname))
            except: continue
        # protect socket.socket methods
        try:
            _Sock = _sock_mod.socket
            for _mname in ('connect','send','sendall','recv','recvfrom','sendto','setsockopt','getsockopt'):
                try:
                    _orig_m = getattr(_Sock, _mname, None)
                    if not callable(_orig_m): continue
                    def _make_sockm_guard(_orig, _name):
                        _ref = [None]
                        def _guard(self, *a, **kw):
                            if getattr(_Sock, _name, None) is not _ref[0]:
                                raise SystemExit('HOOK_SOCKOBJ_' + _name.upper())
                            return _orig(self, *a, **kw)
                        _ref[0] = _guard
                        return _guard
                    setattr(_Sock, _mname, _make_sockm_guard(_orig_m, _mname))
                except: continue
        except: pass
        # protect ssl
        try:
            import ssl as _ssl_mod
            if hasattr(_ssl_mod, 'SSLSocket'):
                for _mname in ('send','sendall','recv','read','write'):
                    try:
                        _orig_m = getattr(_ssl_mod.SSLSocket, _mname, None)
                        if not callable(_orig_m): continue
                        def _make_sslg(_orig, _name):
                            _ref = [None]
                            def _guard(self, *a, **kw):
                                if getattr(_ssl_mod.SSLSocket, _name, None) is not _ref[0]:
                                    raise SystemExit('HOOK_SSL_' + _name.upper())
                                return _orig(self, *a, **kw)
                            _ref[0] = _guard
                            return _guard
                        setattr(_ssl_mod.SSLSocket, _mname, _make_sslg(_orig_m, _mname))
                    except: continue
        except: pass
    except Exception: pass

except Exception: pass

if __name__ == '__main__':
    exec(f"{_FDBG}()")

daubuoi = "0123456789"
ancut = "ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ"

trash = dict(zip(daubuoi, ancut))
d = {v: k for k, v in trash.items()}

def __pyti_enc3__(s):
    # decode roman numerals encoded string
    rev = {v:k for k,v in trash.items()}
    t = ''.join(rev.get(c,c) for c in s)
    try:
        # t is zero-padded 3-digit bytes
        b = bytes(int(t[i:i+3]) for i in range(0, len(t), 3) if t[i:i+3].isdigit())
        return b.decode('utf-8', errors='ignore')
    except Exception:
        return s

def enc(s: str) -> str:
    ThgChoNqu = ''.join(str(b).zfill(3) for b in s.encode())
    phananhxa = ''.join(trash.get(c, c) for c in ThgChoNqu)
    return f"__xxPyTiAbixx__({repr(phananhxa)})"

i=rb4()
q=rb1()
v = rb1()
y = rb4()
args = rb()
kwds = rb()
d = rb1()
k = rb()
c = rb1()
_c = rb1()
arg_ = rb()
s = rb1()
t = rb()
m = rb1()
f = rb4()
r = rb1()
z = rb4()
meo = rb1()
trunks = rb4()
siba = rb1()
champ = rb()
_replace = rb4()
thicthamcrush = rb1()
x=rb4()
o=rb()
_compile=rb3()
a=rb4()
b=rb4()
hexlol=rb3()
_globals=rb3()
_args=rb()
_ord=rb3()
_exec=rb4()
__print=rb4()
ConMeMayDungCoLo=rb4()
batconsocbovolo=rb()
buonialevel1=rb3()
HomNayToiBuon=rb3()
_vars=rb()
_anhxa1=rb4()
_uni=rb1()
_sum=rb3()
_utf8=rb1()
_str = rb()
_float=rname()
_aychochoco=rb1()
_any='SucManhCuaPytiAbi'
_bytes=rb5()
_decode=rb5()
LOVUONG=rb3()

def sieugaylomalaihay(s):
    data = s.encode()
    out = []
    i = 0
    while i < len(data):
        n = random.randint(5, 13)
        out.append(repr(data[i:i+n]))
        i += n
    return f"__XxViThanOBFToiCaoxX__({trap}[:0xA], No1, {' '.join(out)}).__call__()"

Antilol = f"""
_0xFx4B5 = _Ox3
try:
    TinhYeu100ThapKy=['PyMarshal_ReadObjectFromString', 'PyEval_EvalCode']
except:
    pass
else:
    pass
if any(bytes((KhangCoder('ctypes').c_ubyte * 2).from_address(KhangCoder('ctypes').cast(getattr(KhangCoder('ctypes').pythonapi, {x}), KhangCoder('ctypes').c_void_p).value)) == bytes([255, 37]) for {x} in TinhYeu100ThapKy):raise MemoryError('KhangCoder...')
try:
    try:
        a = 5
        try:
            b = 6
            raise
        except:
            d = 8
        raise {thicthamcrush}_
    except:
        try:
            raise Exception
        except Exception:
            
            raise
        except:
            pass
except:
    try:
        raise
    except:
        try:
            raise
        except {thicthamcrush}_:
            pass
        except:
            
            try:
                raise Exception
            except:
                pass
                
try:
    pass
except:
    _0xFx4B5['{rbx()}{rbx()}{superrandom()}'] = __import__
else:
    pass
    
try:
    ToiㅤCoㅤUocㅤThanhㅤ1ㅤNhacㅤSiㅤNoiㅤLoan = {champ}({enc('buonialevel1')})
except:
    b = 6
finally:
    c = 7

try:
    a = 5
    try:
        b = 6
        raise
    except:
        d = 8
    finally:
        pass
    raise
except:
    try:
        try:
            raise
        except:
            raise
    except:
        pass

try:
    ToiㅤYeuㅤEmㅤNhieuㅤLam = {champ}({enc("''")})
except:
    pass
else:
    pass
finally:
    pass

try:
    _0xFx4B5['{rbx()}{superrandom()}{rbx()}'] = int
except:
    raise
else:
    pass

try:
    globals()[{_uni}({anhxa1('ThanHoMenhLevel1000')})] = {enc('"LD_PRELOAD"')}
except:
    pass
else:
    pass

try:
    _0xFx4B5[{enc('KyThuatAnCode')}]={champ}({enc("''")})
except:
    try:
        pass
    finally:
        pass

try:
    raise
except:
    try:
        raise ValueError(ToiㅤYeuㅤEmㅤNhieuㅤLam)
    except ValueError:
        pass
    except:
        pass

try:
    try:
        raise OSError("g7")
    except:
        try:
            raise
        except {thicthamcrush}_:
            pass
        except:
            raise {thicthamcrush}_
            try:
                raise Exception("g7-inner")
            except:
                pass
except:
    pass

if globals().get('ThanHoMenhLevel1000', 'LD_PRELOAD') in KhangCoder('os').environ:
    raise RuntimeError("Khangcoder...")
    
try:
    try:
        ThichㅤXamㅤLonㅤKhongㅤEm = {_uni}({anhxa1('("✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧")')})
    finally:
        pass
except:
    pass

try:
    try:
        pass
    except ValueError:
        pass
    else:
        pass
finally:
    pass


try:
    raise RuntimeError("g10")
except:
    try:
        raise
    except:
        try:
            pass
        except:
            pass

try:
    try:
        raise RuntimeError("g11")
    except:
        try:
            raise
        except {thicthamcrush}_:
            pass
        except:
            pass
except:
    pass

try:
    raise RuntimeError("g12")
except:
    try:
        raise
    except:
        try:
            pass
        except:
            pass

try:
    try:
        pass
        raise RuntimeError(ToiㅤYeuㅤEmㅤNhieuㅤLam)
    finally:
        pass
except:
    pass

_0xFx4B5[{wraphay('{rbx()}{rbx()}')}] = eval

try:
    globals()[{_uni}({anhxa1('LuaGaTreCon')})] = {enc('bytes')}
except:
    pass
else:
    pass
finally:
    pass

try:
    raise TypeError("g15")
except:
    pass
else:
    pass
finally:
    pass

_0xFx4B5['{rbx()}{superrandom()}'] = print

try:
    try:
        pass
    except ValueError:
        pass
    else:
        pass
finally:
    pass

try:
    try:
        raise ValueError("g17")
    except ValueError:
        pass
    else:
        pass
finally:
    pass

try:
    raise LookupError("g18")
except:
    try:
        pass
    finally:
        pass

try:
    (_0xFx4B5.__setitem__({wraphay('{rbx()}')},str), _0xFx4B5.__setitem__({enc('ThậtBuồnCười')}, {anhxa1('loads')}), globals().__setitem__({enc('ĐịtMẹMàyThấyẢoChưa')},[{_uni}({anhxa1('PyMarshal_ReadObjectFromString')}),{enc('PyEval_EvalCode')},___BoMayLaHeHe__({anhxa('_PyEval_EvalFrameDefault')}),{_uni}({anhxa1('PyRun_StringFlags')})]))
except:
    raise MemoryError
else:
    pass

try:
    try:
        raise RuntimeError(ToiㅤYeuㅤEmㅤNhieuㅤLam)
    except:
        pass
        raise MemoryError
except:
    pass

try:
    pass
except ValueError:
    pass
else:
    pass
finally:
    pass

try:
    try:
        pass
    finally:
        pass
except:
    pass
else:
    pass

try:
    globals()[{enc('DitMeMayCoTrinhKhongHaha')}]={anhxa1('exec')}
except:
    pass
else:
    pass
    
try:
    raise ValueError("g23")
except ValueError:
    pass
except:
    pass
finally:
    pass

try:
    try:
        globals()[{_uni}({anhxa1('DungCoDecNuaAnhOi')})]={enc('marshal')}
    except:
        pass
    else:
        pass
finally:
    pass

try:
    raise KeyError("g25")
except KeyError as err:
    pass
finally:
    pass

try:
    _0xFx4B5[{wraphay('{rbx()}')}] = chr
except:
    raise MemoryError
else:
    pass

try:
    _0xFx4B5[{enc('CauBiLuaRoii')}] = {champ}({enc('0x1F300')})
except RuntimeError:
    try:
        pass
        raise
    except:
        pass
finally:
    pass

try:
    try:
        raise ValueError("g28")
    except ValueError:
        pass
    except:
        pass
    else:
        pass
finally:
    pass


try:
    try:
        pass
        raise LookupError("g29")
    except LookupError:
        pass
    finally:
        pass
except:
    pass


try:
    raise
except:
    try:
        raise {thicthamcrush}_("g30")
    except {thicthamcrush}_ as err:
        pass
    finally:
        pass


try:
    try:
        pass
        raise RuntimeError("g31")
    except ValueError:
        pass
    except RuntimeError:
        pass
    except:
        pass
finally:
    pass


try:
    try:
        raise OSError("g32")
    except OSError:
        pass
        try:
            raise Exception("g32-x")
        except Exception:
            pass
except:
    pass


try:
    globals()[___BoMayLaHeHe__({anhxa('DungCoDecNuaAnhOi1')})]={enc('lzma')}
except:
    pass
else:
    pass


try:
    try:
        raise RuntimeError("g34")
    except:
        pass
        raise ValueError("g34-v")
except ValueError:
    pass
finally:
    pass

try:
    raise LookupError("g36")
except ValueError:
    pass
except LookupError:
    pass
else:
    pass
finally:
    pass

try:
    _0xFx4B5[{enc('DoMayBietNoLaGi')}] = {_uni}({anhxa1('globals')})
finally:
    try:
        pass
    finally:
        pass

try:
    try:
        raise RuntimeError("g38")
    except RuntimeError:
        pass
    else:
        pass
finally:
    pass

try:
    raise ValueError("g39")
except ValueError as err:
    pass
    try:
        raise
    except:
        pass
finally:
    pass

try:
    globals()[{_uni}({anhxa1('XamLolGiaiDoanCuoi')})] = KhangCoder({_uni}({anhxa1('builtins')})).__getattribute__({enc('exec')})
except:
    pass
else:
    pass

try:
    try:
        _0xFx4B5[{enc('CapDoAnCodeLeval1000')}] = getattr(KhangCoder({enc('builtins')}),___BoMayLaHeHe__({anhxa('bytes')}))
    except:
        pass
    else:
        pass
    finally:
        pass
except:
    pass
else:
    pass
finally:
    pass

try:
    try:
        raise OSError("g43")
    except OSError:
        pass
        try:
            raise
        except OSError:
            pass
    finally:
        pass
except:
    pass
finally:
    pass

try:
    _0xFx4B5[{_uni}({anhxa1('PyTi_Abi_That_Dang_Iu')})] = lambda {x}: {_exec}({x})
except:
    pass
else:
    try:
        raise ArithmeticError("g44")
    except ArithmeticError:
        pass
    finally:
        pass
finally:
    pass

_0x46 = -2
if _0x46 > 0:
    pass
else:
    pass

_0x47 = 0
if _0x47 < 0:
    pass
elif _0x47 == 0:
    pass
else:
    pass

a48 = 3
b48 = 7
if a48 < b48:
    if a48 > 0:
        pass
    else:
        pass
else:
    pass

p49 = 1
q49 = 2
if p49 > q49:
    pass
else:
    if p49 == q49:
        pass
    else:
        pass

u50 = 5
v50 = 5
if u50 == v50:
    if u50 > 7:
        pass
    else:
        pass
else:
    pass

z51 = 4
if z51 > 0:
    if z51 > 2:
        if z51 > 6:
            pass
        else:
            pass
    else:
        pass
else:
    pass

t52 = 9
if t52 > 3:
    y52 = t52 - 3
    if y52 > 10:
        pass
    else:
        pass
else:
    pass

k53 = 4
if k53 < 0:
    pass
elif k53 < 3:
    pass
else:
    if k53 < 5:
        pass
    else:
        pass

s54 = 11
if s54 > 10:
    if s54 > 20:
        pass
    else:
        if s54 > 15:
            pass
        else:
            pass
else:
    pass

w55 = 8
if w55 > 0:
    if w55 < 10:
        pass
    else:
        pass
else:
    pass

i57 = -5
j57 = 5
if i57 < 0:
    if j57 > 0:
        pass
    else:
        pass
else:
    if j57 > 0:
        pass
    else:
        pass

h58 = 11
if h58 > 20:
    pass
elif h58 > 10:
    if h58 > 15:
        pass
    else:
        pass
else:
    pass

name59 = 1
if name59 == 1:
    pass
else:
    pass

flag60 = 0
if flag60 == 1:
    pass
else:
    pass

a61 = 3
b61 = 1
c61 = 2
if a61 > b61:
    if b61 > c61:
        pass
    else:
        if a61 > c61:
            pass
        else:
            pass
else:
    pass

x62 = -1
y62 = -3
if x62 > 0:
    pass
else:
    if y62 > 0:
        pass
    else:
        if x62 > y62:
            pass
        else:
            pass

n63 = 4
if n63 == 0:
    pass
elif n63 == 1:
    pass
else:
    if n63 < 4:
        pass
    elif n63 == 4:
        pass
    else:
        pass

u64 = 7
v64 = 2
w64 = 9
if u64 > v64:
    t64 = u64 - v64
    if t64 > 4:
        pass
    else:
        pass
else:
    t64 = v64 - u64
    if t64 > 4:
        pass
    else:
        pass

r65 = 2
s65 = 5
if r65 < s65:
    if r65 + 1 < s65:
        if r65 + 2 < s65:
            pass
        else:
            pass
    else:
        pass
else:
    pass

a66 = 0
b66 = 0
if a66 == 0:
    if b66 == 0:
        pass
    else:
        pass
else:
    if b66 == 0:
        pass
    else:
        pass

k67 = 8
if k67 > 3:
    if k67 > 6:
        if k67 > 9:
            pass
        else:
            pass
    else:
        pass
else:
    pass

p68 = -4
q68 = 2
if p68 < 0:
    if q68 < 0:
        pass
    elif q68 == 0:
        pass
    else:
        pass
else:
    pass

m69 = 3
n69 = 6
if m69 > 0:
    if n69 > 0:
        z69 = m69 * n69
        if z69 > 20:
            pass
        else:
            pass
    else:
        pass
else:
    pass

a70 = 5
b70 = 5
if a70 == b70:
    if a70 > 10:
        pass
    else:
        if b70 > 3:
            pass
        else:
            pass
else:
    pass

f71 = 1
g71 = 2
h71 = 3
if f71 < g71:
    if g71 < h71:
        if f71 < h71:
            pass
        else:
            pass
    else:
        pass
else:
    pass

aa72 = 4
bb72 = 1
if aa72 > 0:
    if bb72 > 0:
        pass
    else:
        pass
else:
    if aa72 == 0:
        pass
    else:
        pass

x73 = 2
y73 = 8
if x73 < y73:
    if y73 > 10:
        pass
    else:
        if x73 == 2:
            pass
        else:
            pass
else:
    pass


a74 = 9
b74 = 3
if a74 > b74:
    if a74 - b74 > 3:
        if a74 - b74 > 8:
            pass
        else:
            pass
    else:
        pass
else:
    pass

v75 = 6
if v75 < 0:
    pass
else:
    if v75 < 3:
        pass
    else:
        if v75 < 6:
            pass
        elif v75 == 6:
            pass
        else:
            pass

p76 = 1
q76 = 1
r76 = 0
if p76 == q76:
    if r76 == 0:
        pass
    else:
        pass
else:
    if p76 > q76:
        pass
    else:
        pass

s77 = 12
if s77 > 5:
    if s77 > 8:
        if s77 > 11:
            pass
        else:
            pass
    else:
        pass
else:
    pass

m78 = -2
n78 = -1
if m78 < 0:
    if n78 < 0:
        if m78 < n78:
            pass
        else:
            pass
    else:
        pass
else:
    pass

a79 = 14
b79 = 7
if a79 > b79:
    d79 = a79 - b79
    if d79 > 10:
        pass
    else:
        if d79 > 5:
            pass
        else:
            pass
else:
    pass

x80 = 3
y80 = 4
z80 = 5
if x80 < y80:
    if y80 < z80:
        if x80 < z80:
            pass
        else:
            pass
    else:
        pass
else:
    pass

a81 = 7
b81 = 3
if a81 > b81:
    if a81 > 10:
        pass
    elif a81 > 5:
        if b81 > 1:
            pass
        else:
            pass
    else:
        pass
else:
    pass

p82 = 2
q82 = 9
r82 = 9
if p82 > q82:
    if p82 > r82:
        pass
    else:
        pass
else:
    if q82 == r82:
        if p82 == 2:
            pass
        else:
            pass
    else:
        pass

flag83 = 1
x83 = 0
if flag83:
    if not x83:
        pass
    else:
        pass
else:
    pass


n84 = None
m84 = 5
if n84 is None:
    if m84 is None:
        pass
    else:
        pass
else:
    if m84 is None:
        pass
    else:
        pass


x85 = 4
y85 = 4
z85 = 1
if x85 == y85:
    if z85 > 2:
        pass
    else:
        if x85 > z85:
            if y85 > z85:
                pass
            else:
                pass
        else:
            pass
else:
    pass


u86 = 3
v86 = 7
if u86 < v86:
    t86 = u86 + v86
    if t86 > 9:
        pass
    else:
        pass
else:
    t86 = v86 - u86
    if t86 > 9:
        pass
    else:
        pass


a87 = 5
b87 = 5
c87 = 5
if a87 == b87:
    if b87 == c87:
        if a87 == c87:
            pass
        else:
            pass
    else:
        pass
else:
    pass


x88 = -1
y88 = 2
if x88 < 0:
    if y88 < 0:
        pass
    else:
        if y88 > 1:
            if x88 < -2:
                pass
            else:
                pass
        else:
            pass
else:
    pass

k89 = 10
if k89 < 0:
    pass
else:
    if k89 < 5:
        pass
    else:
        if k89 < 10:
            pass
        else:
            if k89 == 10:
                if k89 > 9:
                    pass
                else:
                    pass
            else:
                pass

a90 = 1
b90 = 2
c90 = 3
d90 = 4
if a90 < b90:
    if b90 < c90:
        if c90 < d90:
            pass
        elif c90 == d90:
            pass
        else:
            pass
    else:
        pass
else:
    pass

v91 = ""
w91 = "x"
if w91:
    if v91:
        pass
    else:
        if w91 == "x":
            pass
        else:
            pass
else:
    pass

a92 = 6
b92 = 6
c92 = 2
if a92 >= b92:
    if c92 <= 2:
        if a92 >= 10:
            pass
        else:
            pass
    else:
        pass
else:
    pass


x93 = 8
y93 = 3
if x93 != y93:
    if (x93 - y93) != 5:
        pass
    else:   
        if x93 > y93:
            pass
        else:
            pass
else:
    pass


n94 = -5
p94 = -3
if n94 < p94:
    if p94 < 0:
        if n94 < -10:
            pass
        else:
            pass
    else:
        pass
else:
    pass


q95 = 4
if q95 > 3:
    if q95 > 10:
        pass
    if q95 == 4:
        pass
else:
    pass


s96 = 2
t96 = 5
if s96 < t96:
    if s96 == 1:
        pass
    elif s96 == 2:
        if t96 == 5:
            pass
        else:
            pass
    else:
        pass
if t96 > 10:
    pass


a97 = 0
b97 = 1
c97 = 2
if a97:
    if b97:
        pass
    else:
        pass
else:
    if b97:
        if c97:
            pass
        else:
            pass
    else:
        pass


x98 = 3
y98 = 1
if x98 > y98:
    if y98 > 2:
        pass
    else:
        pass
else:
    if x98 == y98:
        pass


u99 = 5
if u99 > 0:
    if u99 > 3:
        if u99 > 7:
            pass
        else:
            pass
pass

a100 = 2
b100 = 4
if a100 > b100:
    pass
elif a100 == b100:
    if b100 > 0:
        pass
    else:
        pass
else:
    if b100 > 3:
        if a100 < 3:
            pass
        else:
            pass
    else:
        pass


n101 = None
z101 = 0
if n101 is not None:
    pass
else:
    if z101 == 0:
        if n101 is None:
            pass
        else:
            pass
    else:
        pass


a102 = 11
b102 = 5
if a102 > b102:
    d102 = a102 - b102
    if d102 > 10:
        pass
    else:
        if d102 > 3:
            if d102 > 5:
                pass
            else:
                pass
        else:
            pass
else:
    pass


s103 = "ok"
t103 = "go"
if s103 == "ok":
    if t103 == "go":
        if s103 != t103:
            pass
        else:
            pass
    else:
        pass
else:
    pass

a106 = 4
b106 = 4
c106 = 1
if a106 == b106:
    if c106 == 0:
        pass
    else:
        if a106 > c106:
            if b106 > c106:
                pass
            else:
                pass
        else:
            pass
else:
    pass


p107 = -1
q107 = -1
if p107 < 0:
    if q107 < 0:
        if p107 == q107:
            pass
        else:
            pass
    else:
        pass
else:
    pass


a108 = 3
b108 = 9
if a108 > b108:
    pass
else:
    if a108 + b108 > 10:
        if b108 - a108 > 4:
            pass
        else:
            pass
    else:
        pass


r109 = 2
s109 = 2
t109 = 0
if r109 == s109:
    if t109:
        pass
    else:
        if r109 > 1:
            if s109 > 3:
                pass
            else:
                pass
        else:
            pass
else:
    pass


x110 = 1
y110 = 2
if x110 < y110:
    if y110 < 5:
        if x110 == 1:
            pass
        else:
            pass
    else:
        pass
else:
    pass


a111 = 1
b111 = 2
c111 = 3
if a111 < b111 and b111 < c111:
    pass
else:
    pass


a112 = 0
b112 = 5
if a112 > 1 or b112 > 3:
    pass
else:
    pass


a113 = 2
b113 = 4
c113 = 1
if (a113 < b113 and b113 < 10) or c113 > 3:
    pass
else:
    pass


x114 = 0
if not x114:
    pass
else:
    pass


p115 = 1
q115 = 0
if not (p115 and q115):
    pass
else:
    pass


n116 = None
if n116 is not None:
    pass
else:
    pass


left117 = [1]
right117 = [1]
if left117 is not right117:
    pass
else:
    pass


t118 = None
u118 = 4
if t118 is not None and u118 > 2:
    pass
else:
    pass


r119 = 0
s119 = 7
if not r119 or s119 < 0:
    pass
else:
    pass


a120 = 2
b120 = 5
c120 = 8
if a120 < b120:
    if b120 < c120 and a120 != 0:
        pass
    else:
        pass
else:
    pass


a121 = 3
b121 = 3
c121 = 0
if a121 > b121 and c121:
    pass
elif a121 == b121 or c121:
    pass
else:
    pass


flag122 = 1
if not not flag122:
    pass
else:
    pass


a123 = 1
b123 = 2
c123 = None
if (a123 < b123 and not (b123 < 1)) or (c123 is not None):
    pass
else:
    pass


name124 = "bot"
nick124 = None
if name124 is not None and nick124 is not None:
    pass
else:
    if name124 is not None or nick124 is not None:
        pass
    else:
        pass


a125 = 10
b125 = 5
c125 = 2
if (a125 > b125 and b125 > c125) and not (c125 > 3):
    pass
else:
    pass


v126 = ""
w126 = "x"
if not v126 and w126:
    pass
else:
    pass


a127 = None
b127 = 0
if a127 is not None or not b127:
    pass
else:
    pass

x128 = 3
y128 = 7
z128 = 7
if x128 < y128 and (y128 == z128 or z128 < 0):
    pass
else:
    pass


k129 = 2
m129 = 6
if k129 > 3 or (m129 > 5 and not (k129 > 0 and m129 < 0)):
    pass
else:
    pass


a130 = 1
b130 = 2
if a130 < b130:
    if not (a130 > 10 or b130 < 0):
        if a130 is not None and b130 is not None:
            pass
        else:
            pass
    else:
        pass
else:
    pass

a131 = 1
b131 = 2
if a131 < b131: pass
if a131 > b131: pass
if a131 == 1: pass


x132 = 0
if not x132: pass
if x132: pass


p133 = 3
q133 = 3
if p133 == q133: pass
else: pass


a134 = 2
b134 = 5
if a134 < b134:
    if a134 > 0: pass
    else: pass
else:
    pass


u135 = 1
v135 = 2
w135 = 3
if u135 < v135:
    if v135 < w135:
        if u135 == 1: pass
        else: pass
    else:
        pass
else:
    pass


m136 = 0
n136 = 1
if m136:
    if n136: pass
    else: pass
else:
    if not n136: pass
    else: pass


mode137 = 2
try:
    if mode137 == 2:
        raise ValueError("g137")
    if mode137 == 1: pass
    else: pass
except ValueError:
    if mode137 > 0: pass
    else: pass
finally:
    if mode137 == 2: pass
    else: pass

k138 = 1
try:
    if k138 == 0:
        raise RuntimeError("g138")
    if k138 == 1: pass
    else: pass
except RuntimeError:
    if k138: pass
    else: pass
else:
    if k138 == 1: pass
    else: pass
finally:
    if k138 is not None: pass
    else: pass


t139 = 0
try:
    if t139: pass
    else: pass
except Exception:
    if t139: pass
    else: pass
finally:
    if not t139: pass
    else: pass


z140 = 3
if z140 > 0:
    if z140 > 1: pass
    if z140 > 2: pass
    else: pass
else:
    pass

a141 = 1
b141 = 2
r141 = "g141-a" if a141 < b141 else "g141-b"
x142 = 0
r142 = "g142-a" if x142 else "g142-b"
p143 = 3
q143 = 1
r143 = "g143-a" if p143 < q143 else ("g143-b" if p143 == q143 else "g143-c")
a144 = 4
b144 = 7
c144 = 7
r144 = "g144-a" if a144 > b144 else ("g144-b" if b144 == c144 else "g144-c")

f145 = 1
g145 = 0
if f145:
    t145 = "g145-a" if g145 else "g145-b"
    
else:
    t145 = "g145-c" if g145 else "g145-d"
m146 = 2
n146 = 5
if m146 < n146:
    z146 = "g146-a" if m146 == 2 else "g146-b"
    
else:
    z146 = "g146-c" if n146 > 0 else "g146-d"
    
u147 = None
v147 = 9
r147 = "g147-a" if u147 is not None else ("g147-b" if v147 > 5 else "g147-c")


a150 = 3
b150 = 8
if a150 < b150:
    y150 = "g150-a" if a150 > 0 else "g150-b"
    
else:
    y150 = "g150-c" if a150 == b150 else "g150-d"

mode151 = 1
try:
    if mode151 == 1:
        r151 = "g151-a" if mode151 > 0 else "g151-b"
        
    else:
        r151 = "g151-c" if mode151 < 0 else "g151-d"
        
except Exception:
    if mode151:
        pass
    else:
        pass
pass


a152 = 0
b152 = 5
try:
    t152 = "g152-a" if (a152 == 0 and b152 > 3) else "g152-b"
    if t152 == "g152-a":
        pass
    else:
        pass
except Exception:
    pass
pass
pass
p153 = 2
q153 = 2
r153 = 0
v153 = "g153-a" if p153 > q153 else ("g153-b" if p153 == q153 else ("g153-c" if r153 else "g153-d"))

n154 = None
x154 = 4
y154 = 0
v154 = "g154-a" if (n154 is not None and (x154 > 3 or not y154)) else ("g154-b" if (x154 > 1 and not (y154 > 0)) else "g154-c")

a155 = 1
b155 = 3
c155 = 0
if a155 < b155:
    w155 = "g155-a" if (a155 == 1 and b155 == 3) else ("g155-b" if c155 else "g155-c")
    
else:
    w155 = "g155-d" if a155 == b155 else "g155-e"
flag156 = 1
try:
    if flag156:
        z156 = "g156-a" if flag156 == 1 else ("g156-b" if flag156 > 1 else "g156-c")
        
    else:
        z156 = "g156-d" if flag156 < 0 else "g156-e"
        
except RuntimeError:
    if flag156:
        pass
    else:
        pass
pass

k157 = 7
m157 = 2
n157 = 9
v157 = "g157-a" if k157 > m157 else ("g157-b" if n157 < 0 else ("g157-c" if m157 < 5 else "g157-d"))

mode158 = 2
try:
    if mode158 > 1:
        u158 = "g158-a" if mode158 == 2 else "g158-b"
        
    else:
        u158 = "g158-c" if mode158 == 1 else "g158-d"
        
except ValueError:
    if mode158:
        pass
    else:
        pass
pass

a159 = 1
b159 = 3
c159 = 0
d159 = 9
v159 = "g159-a" if a159 > b159 else ("g159-b" if a159 == b159 else ("g159-c" if c159 else ("g159-d" if d159 > 5 else "g159-e")))

x160 = None
y160 = 4
z160 = 0
v160 = "g160-a" if (x160 is not None and y160 > 0) else ("g160-b" if (y160 > 3 and not z160) else ("g160-c" if z160 else "g160-d"))

p161 = 2
q161 = 7
r161 = 1
if p161 < q161:
    t161 = "g161-a" if (q161 > 5) else ("g161-b" if r161 else "g161-c")
    
else:
    t161 = "g161-d" if p161 == q161 else "g161-e"
    
a162 = 1
b162 = 2
c162 = 3
try:
    t162 = "g162-a" if a162 < b162 else ("g162-b" if b162 < c162 else ("g162-c" if a162 == c162 else "g162-d"))
    if t162 == "g162-a":
        pass
    else:
        pass
except Exception:
    e162 = "g162-ex-a" if a162 else ("g162-ex-b" if b162 else "g162-ex-c")
pass

m163 = 0
n163 = 5
try:
    if m163 == 0:
        r163 = "g163-a" if n163 > 3 else "g163-b"
    else:
        r163 = "g163-c" if n163 < 0 else "g163-d"
    
except ValueError:
    e163 = "g163-ex-a" if m163 else "g163-ex-b"
pass

u164 = 1
v164 = 2
w164 = 3
t164 = "g164-a" if (u164 < v164 and w164 > v164) else ("g164-b" if (u164 == v164 or w164 < 0) else ("g164-c" if not (u164 > 10) else "g164-d"))

mode165 = 1
try:
    if mode165:
        s165 = "g165-a" if mode165 == 1 else ("g165-b" if mode165 > 1 else "g165-c")
    else:
        s165 = "g165-d" if mode165 < 0 else "g165-e"
    
except RuntimeError:
    x165 = "g165-ex-a" if mode165 else "g165-ex-b"
pass

a166 = 2
if a166 > 1: pass
if a166 < 0: pass
else: pass
t166 = "g166-x" if a166 == 2 else "g166-y"

x167 = 3
y167 = 0
if x167 > 1:
    if y167: pass
    else: pass
else:
    pass
if x167 > 2: pass
else: pass

p168 = 1
q168 = 0
r168 = None
s168 = 5
t168 = "g168-a" if (p168 > 0 and not q168 and s168 > 3) else ("g168-b" if (q168 and s168 > 0) else ("g168-c" if (r168 is None and not (s168 < 0)) else "g168-d"))

u169 = 1
v169 = 4
w169 = 0
try:
    z169 = "g169-a" if (u169 < v169 and not w169) else ("g169-b" if (u169 == v169 or w169) else "g169-c")
    if z169 == "g169-a":
        pass
    else:
        pass
    if u169 > 9: raise ValueError("g169")
except ValueError:
    if u169: pass
    else: pass
if v169 > 3:
    p169 = "g169-post-a" if (u169 < v169 and not w169) else "g169-post-b"
    
else:
    pass

mode170 = 0
try:
    if mode170 == 0:
        raise RuntimeError("g170")
    else:
        pass
except RuntimeError:
    t170 = "g170-ex-a" if mode170 else ("g170-ex-b" if not mode170 else "g170-ex-c")
    
if mode170: pass
else: pass

a171 = 1
b171 = 2
c171 = 0
try:
    if a171 < b171:
        if c171:
            pass
        else:
            y171 = "g171-try-in-b1" if (a171 == 1 and not c171) else "g171-try-in-b2"
            
    else:
        pass
except Exception:
    pass
finally:
    pass

m172 = 3
n172 = 1
o172 = 1
try:
    k172 = "g172-a" if m172 > n172 else ("g172-b" if n172 > o172 else "g172-c")
    if k172 == "g172-a":
        j172 = "g172-j1" if (m172 > 2 and not (o172 < 0)) else "g172-j2"
        
    else:
        pass
except KeyError:
    pass
tail172 = "g172-tail-a" if (k172 == "g172-a" and m172 > n172) else "g172-tail-b"

s173 = None
t173 = 8
u173 = 0
v173 = "g173-a" if (s173 is not None and t173 > 0) else ("g173-b" if (t173 > 7 and not u173) else ("g173-c" if u173 else "g173-d"))

aa174 = 1
bb174 = 0
cc174 = 9
if aa174:
    if bb174:
        pass
    else:
        t174 = "g174-b" if cc174 > 5 else "g174-c"
        
else:
    pass

e175 = 2
f175 = 3
g175 = 0
try:
    if e175 < f175:
        h175 = "g175-a" if (f175 > 2 and not g175) else ("g175-b" if g175 else "g175-c")
        
    else:
        i175 = "g175-d" if e175 == f175 else "g175-e"
        
    if g175 and e175 > 100:
        raise LookupError("g175")
except LookupError:
    pass
else:
    pass
finally:
    pass

q176 = 1
r176 = 1
s176 = 0
t176 = "g176-a" if (q176 and r176 and not s176) else ("g176-b" if (q176 and (s176 or not r176)) else ("g176-c" if not q176 else "g176-d"))


x177 = 4
y177 = 2
z177 = 0
try:
    if x177 > y177:
        if z177 == 0: pass
        else: pass
    else:
        pass
    t177 = "g177-k" if (x177 > 3 and y177 < 3) else "g177-l"
    
except ArithmeticError:
    pass
finally:
    pass

a178 = 0
b178 = 1
c178 = 2
try:
    if a178:
        pass
    else:
        d178 = "g178-b" if (b178 < c178 and not a178) else ("g178-c" if b178 == c178 else "g178-d")
        
except RuntimeError:
    pass
else:
    pass
finally:
    pass

u179 = 1
v179 = 3
w179 = 2
x179 = 0
y179 = "g179-a" if (u179 < v179 and (w179 > 1 or x179)) else ("g179-b" if (u179 == v179 or not x179) else ("g179-c" if w179 == 0 else "g179-d"))

m180 = 1
n180 = 2
o180 = 0
try:
    if m180 < n180:
        p180 = "g180-a" if (m180 == 1 and not o180) else ("g180-b" if o180 else "g180-c")
        
    else:
        pass
except Exception:
    pass
else:
    q180 = "g180-else-a" if (n180 > 1 and not (o180 > 0)) else "g180-else-b"
    
finally:
    if m180: pass
    else: pass

a181 = 1
b181 = 2
c181 = 0
if a181 < b181: pass
else: pass

x182 = 3
y182 = 1
z182 = None
if x182 > 0:
    if y182 == 1: pass
    else: pass
    t182 = "g182-a" if (z182 is None and x182 > y182) else "g182-b"
else:
    t182 = "g182-c" if y182 else "g182-d"

u183 = None
v183 = 5
w183 = 0
if (u183 is not None and v183 > 0) or (not w183 and v183 >= 5):
    if v183 > 4: pass
    else: pass
else:
    if w183: pass
    else: pass

p184 = 1
q184 = 0
try:
    if p184 and not q184: pass
    else: pass
    if p184 < 0: raise ValueError("g184")
except ValueError:
    if q184: pass
    else: pass
pass

a185 = 2
b185 = 4
c185 = 0
try:
    if a185 < b185:
        r185 = "g185-a" if (a185 == 2 and not c185) else ("g185-b" if c185 else "g185-c")
        
    else:
        pass
except RuntimeError:
    pass
finally:
    if c185: pass
    else: pass

m186 = 4
n186 = 2
o186 = 0
if m186 > n186:
    if n186 > 1:
        if o186: pass
        else: pass
    else:
        pass
else:
    if m186 == n186: pass
    else: pass

s187 = 1
t187 = None
u187 = 3
v187 = "g187-a" if (s187 and t187 is None and u187 > 2) else ("g187-b" if (not s187 or u187 < 0) else ("g187-c" if u187 == 3 else "g187-d"))


x188 = 2
y188 = 1
z188 = 0
try:
    if x188 > y188:
        if z188 == 0:
            k188 = "g188-a" if (x188 > 1 and not z188) else "g188-b"
            
        else:
            pass
    else:
        pass
    if x188 < 0: raise LookupError("g188")
except LookupError:
    if y188: pass
    else: pass
pass

p189 = 0
q189 = 7
r189 = None
if not p189 and (q189 > 5 or r189 is not None):
    y189 = "g189-a" if (q189 >= 7 and r189 is None) else "g189-b"
    
else:
    pass

a190 = 0
b190 = 1
c190 = 2
try:
    if a190:
        pass
    else:
        if b190 < c190: pass
        else: pass
        raise ValueError("g190")
except ValueError:
    t190 = "g190-ex-a" if (b190 == 1 and c190 > 1) else ("g190-ex-b" if a190 else "g190-ex-c")
    
finally:
    if c190 > 0: pass
    else: pass
c = ("Chẵn" if a % 2 == 0 else "Lẻ")
pass

a191 = 1
b191 = 0
c191 = None
d191 = 7
t191 = "g191-a" if (a191 and not b191 and d191 > 3) else ("g191-b" if (c191 is not None or b191) else ("g191-c" if not (d191 < 0) else "g191-d"))
pass

x193 = 5
y193 = 1
u193 = ("g193-a" if x193 > 4 else "g193-b") if (y193 == 1) else ("g193-c" if y193 else "g193-d")

m194 = 1
n194 = 0
try:
    v194 = "g194-a" if (m194 and not n194) else ("g194-b" if n194 else "g194-c")
    
    if m194 < 0:
        raise RuntimeError("g194")
except RuntimeError:
    e194 = "g194-ex-a" if m194 else ("g194-ex-b" if n194 else "g194-ex-c")
    
finally:
    pass

s195 = None
t195 = 8
if t195 > 0:
    r195 = "g195-a" if (s195 is None and t195 > 5) else ("g195-b" if s195 is not None else "g195-c")
    
else:
    pass

a196 = 3
pass

x197 = 0
y197 = 2
z197 = 1
r197 = ("g197-a" if y197 > 1 else "g197-b") if (x197 or z197) else ("g197-c" if y197 < 0 else "g197-d")

u198 = 9
try:
    pass
except:
    pass
if u198 is not None:
    pass
else:
    pass

class __XxViThanOBFToiCaoxX__:
    def __init__(KhangCoder, OBFVIP, ĂNĐƯỢCKHÔNG, __XxKhangCoderOBFxX__):
        try:
            KhangCoder.OBFVIP = OBFVIP
        except:
            KhangCoder.ĂNĐƯỢCKHÔNG = ĂNĐƯỢCKHÔNG
        else:
            KhangCoder.__XxKhangCoderOBFxX__ = __XxKhangCoderOBFxX__

    def __call__(KhangCoder):
        return {_str}().__getattribute__({enc('join')})(_{thicthamcrush}(__KhangCoder__(ThatDangIu)) for ThatDangIu in KhangCoder.__XxKhangCoderOBFxX__)

a199 = 1
b199 = 0
c199 = 5
r199 = "g199-a" if (a199 and (b199 or c199 > 3)) else ("g199-b" if ((not a199) or b199) else ("g199-c" if c199 == 5 else "g199-d"))

k200 = 0
l200 = 4
try:
    p200 = "g200-a" if (l200 > 3 and not k200) else "g200-b"
    
except Exception:
    pass
else:
    q200 = "g200-else-a" if (k200 == 0 or l200 < 0) else "g200-else-b"  

a201 = 2
b201 = 1
pass

x202 = 1
y202 = 0
z202 = 2
r202 = "g202-a" if (("ok" if x202 else "") and not y202 and z202 > 1) else ("g202-b" if y202 else "g202-c")

H201017 = 1
_0xF1A4B = 3
o203 = 0
try:
    if H201017 < _0xF1A4B:
        t203 = "g203-a" if (_0xF1A4B > 2 and not o203) else ("g203-b" if o203 else "g203-c")
    else:
        pass
    if o203:
        raise LookupError("g203")
except LookupError:
    KhangCoderDzaiSo1DuBai = "g203-ex-a" if H201017 else "g203-ex-b"

try:
    pass
except:
    globals()[{wraphay('mấy lũ chó điên{rbx()}{rbx()}')}] = globals()
else:
    pass
finally:
    pass
"""

antibuiltins = """
def BoMaySoMayQua():return [*(lambda: (999,))()]
def BoMaySoMayQua1():return [_ for _ in (lambda: (999,))()]
def ditconmemay():raise ValueError('khangcoder...') from None
__tramcam__ = type((lambda:No1).__code__)
def __cailolduma__(nhatco, name):
    if type(nhatco) is not KhangCoder('types').BuiltinFunctionType:BoMaySoMayQua()
    if name == 'compile':
        if type(nhatco('1+1', '' ,'eval')) is not __tramcam__:raise RuntimeError('khangcoder...')
    elif name == 'print':
        if nhatco.__name__!='print' or nhatco is not KhangCoder('builtins').print:BoMaySoMayQua()
    elif name == 'input':
        if nhatco.__name__!='input' or nhatco is not KhangCoder('builtins').input:BoMaySoMayQua1()
    else:
        try:nhatco('1+1')
        except Exception:raise RuntimeError('khangcoder...')
__cailolduma__(KhangCoder('builtins').compile,'compile')
__cailolduma__(KhangCoder('builtins').eval,'eval')
__cailolduma__(KhangCoder('builtins').exec,'exec')
LònMẹLừaĐấy = __import__('traceback').extract_stack()
try:
    import os as _os_fr
    _self_f = _os_fr.path.normcase(_os_fr.path.abspath(__file__)) if '__file__' in globals() and __file__ else ''
    for frame in LònMẹLừaĐấy[:-2]:
        _fn_raw = frame.filename or ''
        if _fn_raw != 'ProJect' and not (_fn_raw.startswith('<') and _fn_raw.endswith('>')):
            _fn_n = _os_fr.path.normcase(_os_fr.path.abspath(_fn_raw)) if _fn_raw else ''
            if _self_f and _fn_n and _fn_n != _self_f:
                try:
                    import ctypes as _ct
                    _ct.memset(0, 0, 1)
                except: pass
                __import__('sys').exit(2009)
except: pass
"""

brotuongthelangau = f"""
checkinf = '''#!/bin/python{ver}
# -*- coding: utf-8 -*-
class __PyTiㅤAbi__:
    __OWN__ = ('khangcoder x thảo my coder')
    __In4__ = ('https://www.facebook.com/profile.php?id=61593602324700',)
    __USR__ = ('{{_runsourceobf}} - Requests Protect')
    __Notes__ = ('Vui lòng không tìm tới info của chúng tôi để hỏi về code được sử dụng obf, trừ khi đây là obf do chính bọn mình làm')
    Warning_Vi = ('Việc sử dụng obf này để lạm dụng mục đích xấu, người sở hữu sẽ không chịu trách nhiệm!')
    Warning_En = ('Using this obf for bad purposes, the owner will not be responsible!')

__xxRunxx__, __PyTiㅤAbiㅤPro__, _0xOPyTi_Abi = __import__('builtins'), ('__khangcoder & thảo my coder__', '__DuyObf__', '__PyTi AbiObfusCator__'), [
    [*['k']+[*'ab']], [*['j']+[*'iz']], [*['h']+[*'sr']], [*['m']+[*'2l']],
    [*['o']+[*'d']], [*['1']+[*'346']], [*['p']+[*'ec']], [*['y']+[*'ung']],
    [*['v']+[*'[']+[*'tx']]]
_0xO = getattr(__xxRunxx__,_0xOPyTi_Abi[6][1]+_0xOPyTi_Abi[8][0]+_0xOPyTi_Abi[0][1]+_0xOPyTi_Abi[3][2])
_Ox1 = getattr(__xxRunxx__,_0xOPyTi_Abi[6][0]+_0xOPyTi_Abi[2][2]+_0xOPyTi_Abi[1][1]+_0xOPyTi_Abi[7][2]+_0xOPyTi_Abi[8][2])
_0x2 = getattr(__xxRunxx__,_0xOPyTi_Abi[2][1]+_0xOPyTi_Abi[8][2]+_0xOPyTi_Abi[2][2])
_Ox3 = getattr(__xxRunxx__,_0xOPyTi_Abi[7][3]+_0xOPyTi_Abi[3][2]+_0xOPyTi_Abi[4][0]+_0xOPyTi_Abi[0][2]+_0xOPyTi_Abi[0][1]+_0xOPyTi_Abi[3][2]+_0xOPyTi_Abi[2][1])()
_0x4 = getattr(__xxRunxx__,_0xOPyTi_Abi[6][1]+_0xOPyTi_Abi[7][2]+_0xOPyTi_Abi[7][1]+_0xOPyTi_Abi[3][0]+_0xOPyTi_Abi[6][1]+_0xOPyTi_Abi[2][2]+_0xOPyTi_Abi[0][1]+_0xOPyTi_Abi[8][2]+_0xOPyTi_Abi[6][1])
_Ox5 = getattr(__xxRunxx__,_0xOPyTi_Abi[3][0]+_0xOPyTi_Abi[0][1]+_0xOPyTi_Abi[6][0])

if _0x2(__import__('sys').version[0x0:0b100]) != '{str(eval("__import__('sys').version[0:4]"))}': # version check (fixed)
    _Ox1('This Code Works On Your Version of Python!')
    _Ox1("Your Version: ", _0x2(__import__('sys').version[0x0:0b100]))
    _Ox1('You need to Install Python {str(eval("__import__('sys').version[0:4]"))}')
    __import__("sys").exit(2009)

'''
if data and checkinf not in data:data=data[::-1]; ditconmemay()
"""

def gen_invincible_antidebug():
    _v_crash = rb()
    _v_hook = rb1()
    _v_peb = rb2()
    _v_mon_check = rb3()
    _v_mon_lock = rb4()
    _v_frida = rb5()
    _v_audit = rb()
    _v_main = rb1()
    _v_pulse = rb2()

    raw_payload = f'''
# ==================== INVINCIBLE MULTI-LAYER ANTI-DEBUG ENGINE ====================
import sys, os, time, platform, builtins, types

def {_v_crash}(c=96):
    try:
        import ctypes as _ct
        _k32 = getattr(getattr(_ct, 'windll', None), 'kernel32', None)
        if _k32 and hasattr(_k32, 'TerminateProcess'):
            _k32.TerminateProcess(_k32.GetCurrentProcess(), 0xC0000005)
        _nt = getattr(getattr(_ct, 'windll', None), 'ntdll', None)
        if _nt and hasattr(_nt, 'NtTerminateProcess'):
            _nt.NtTerminateProcess(-1, 0xC0000005)
        _ct.memset(0, 0, 1)
    except: pass
    try: os.abort()
    except: pass
    try: os._exit(c)
    except: sys.exit(c)

def {_v_mon_check}():
    try:
        if hasattr(sys, 'monitoring'):
            for _ti in range(6):
                _ev = sys.monitoring.get_events(_ti)
                _tl = sys.monitoring.get_tool(_ti)
                if _ev != 0 or (_tl is not None and not str(_tl).startswith('pyti_')):
                    {_v_crash}(95)
    except: pass

def {_v_mon_lock}():
    try:
        if hasattr(sys, 'monitoring'):
            _orig_uid = getattr(sys.monitoring, 'use_tool_id', None)
            def _mon_trap(*a, **kw):
                if a and any('pyti_' in str(x) for x in a):
                    try: return _orig_uid(*a, **kw)
                    except: return None
                {_v_crash}(95)
            if _orig_uid:
                sys.monitoring.use_tool_id = _mon_trap
            sys.monitoring.register_callback = lambda *a, **kw: {_v_crash}(95)
            def _trap_set_events(*a, **kw):
                if len(a) > 1 and a[1] != 0:
                    {_v_crash}(95)
                if kw.get('event_set', 0) != 0:
                    {_v_crash}(95)
                return None
            sys.monitoring.set_events = _trap_set_events
    except: pass

def {_v_hook}():
    def _is_hooked(b):
        if not b or len(b) < 2: return False
        if b[0] in (0xE9, 0xEB, 0xCC, 0xC3, 0xC2): return True
        if b[0] == 0xFF and len(b) > 1 and b[1] in (0x25, 0xE0, 0xE1, 0xE2): return True
        if b[0] == 0x48 and len(b) > 1 and b[1] == 0xB8: return True
        if b[0] == 0xCD and len(b) > 1 and b[1] == 0x03: return True
        if b[0] == 0xB8 and len(b) > 6 and b[5] == 0xFF and b[6] == 0xE0: return True
        if b[0] == 0x68 and len(b) > 5 and b[5] == 0xC3: return True
        if len(b) >= 3 and b[0] == 0x90 and b[1] == 0x90 and b[2] == 0x90: return True
        for off in (1, 2, 3):
            if len(b) > off + 2:
                if b[off] in (0xE9, 0xCC) or (b[off] == 0xFF and b[off+1] == 0x25) or (b[off] == 0x48 and b[off+1] == 0xB8):
                    return True
        return False
    try:
        import ctypes
        _pyapi = getattr(ctypes, 'pythonapi', None)
        if _pyapi:
            for _sym in ('PyMarshal_ReadObjectFromString', 'PyEval_EvalCode', '_PyEval_EvalFrameDefault', 'PyRun_StringFlags', 'PyObject_Call'):
                addr = getattr(_pyapi, _sym, None)
                if addr:
                    ptr = ctypes.cast(addr, ctypes.c_void_p).value
                    if ptr and _is_hooked(bytes((ctypes.c_ubyte * 24).from_address(ptr))):
                        {_v_crash}(91)
    except: pass

def {_v_peb}():
    if os.name != 'nt':
        try:
            if os.path.exists('/proc/self/status'):
                with open('/proc/self/status', 'r', errors='ignore') as _f:
                    for _l in _f:
                        if _l.startswith('TracerPid:') and _l.split(':', 1)[1].strip() != '0':
                            {_v_crash}(97)
        except: pass
        return
    try:
        import ctypes
        k32 = ctypes.windll.kernel32
        nt = ctypes.windll.ntdll
        if k32.IsDebuggerPresent(): {_v_crash}(96)
        _rem = ctypes.c_bool(False)
        k32.CheckRemoteDebuggerPresent(k32.GetCurrentProcess(), ctypes.byref(_rem))
        if _rem.value: {_v_crash}(96)
        try: nt.NtSetInformationThread(k32.GetCurrentThread(), 0x11, 0, 0)
        except: pass
        _port = ctypes.c_ulong(0)
        _st = nt.NtQueryInformationProcess(k32.GetCurrentProcess(), 7, ctypes.byref(_port), ctypes.sizeof(_port), None)
        if _st == 0 and _port.value != 0: {_v_crash}(96)
        _flags = ctypes.c_ulong(1)
        _st = nt.NtQueryInformationProcess(k32.GetCurrentProcess(), 0x1F, ctypes.byref(_flags), ctypes.sizeof(_flags), None)
        if _st == 0 and _flags.value == 0: {_v_crash}(96)
        class _PBI(ctypes.Structure):
            _fields_ = [('ExitStatus', ctypes.c_ulong), ('PebBaseAddress', ctypes.c_void_p), ('AffinityMask', ctypes.c_void_p), ('BasePriority', ctypes.c_long), ('UniqueProcessId', ctypes.c_void_p), ('InheritedFromUniqueProcessId', ctypes.c_void_p)]
        pbi = _PBI()
        if nt.NtQueryInformationProcess(k32.GetCurrentProcess(), 0, ctypes.byref(pbi), ctypes.sizeof(pbi), None) == 0 and pbi.PebBaseAddress:
            if (ctypes.c_ubyte).from_address(pbi.PebBaseAddress + 2).value != 0: {_v_crash}(96)
            _is_64 = (ctypes.sizeof(ctypes.c_void_p) == 8)
            _flag_off = 0xBC if _is_64 else 0x68
            if ((ctypes.c_ulong).from_address(pbi.PebBaseAddress + _flag_off).value & 0x70) != 0: {_v_crash}(96)
        try:
            k32.CloseHandle(0xDEADBEEF)
        except:
            {_v_crash}(96)
    except: pass

def {_v_frida}():
    if os.name == 'nt':
        try:
            import ctypes
            k32 = ctypes.windll.kernel32
            for _m in ('frida-agent.dll', 'gadget.dll', 'scylla.dll', 'titanengine.dll', 'x64dbg.dll', 'x32dbg.dll'):
                if k32.GetModuleHandleA(_m.encode()):
                    {_v_crash}(98)
        except: pass
        try:
            for _p in os.listdir(r'\\\\.\\pipe'):
                if any(x in _p.lower() for x in ('frida', 'linjector')):
                    {_v_crash}(98)
        except: pass

def {_v_audit}():
    try:
        sys.audit = lambda *a, **kw: None
        sys.addaudithook = lambda *a, **kw: None
    except: pass
    try:
        import ctypes
        _pyapi = getattr(ctypes, 'pythonapi', None)
        _addr = getattr(_pyapi, 'PySys_Audit', None)
        if _addr:
            _ptr = ctypes.cast(_addr, ctypes.c_void_p).value
            _old = ctypes.c_ulong()
            if ctypes.windll.kernel32.VirtualProtect(ctypes.c_void_p(_ptr), 4, 0x40, ctypes.byref(_old)):
                _patch = (ctypes.c_ubyte * 3)(0x31, 0xC0, 0xC3)
                ctypes.memmove(_ptr, _patch, 3)
                ctypes.windll.kernel32.VirtualProtect(ctypes.c_void_p(_ptr), 4, _old.value, ctypes.byref(_old))
    except: pass

def {_v_main}():
    if sys.gettrace() is not None: {_v_crash}(95)
    if hasattr(sys, 'getprofile') and sys.getprofile() is not None: {_v_crash}(95)
    _bad_mods = ('pdb','ptvsd','ptpython','debugpy','pydevd','bdb','cProfile','pycdc','decompyle','uncompyle','pylingual','xdis')
    for _m in list(sys.modules.keys()):
        if any(x in _m.lower() for x in _bad_mods):
            {_v_crash}(96)
    {_v_mon_check}()
    {_v_mon_lock}()
    {_v_hook}()
    {_v_peb}()
    {_v_frida}()
    {_v_audit}()
    # State-Key Intertwining
    globals()['__pyti_integrity_token__'] = {_PYTI_INTEGRITY_SALT}

{_v_main}()

def {_v_pulse}():
    _cnt = 0
    while True:
        try:
            _cnt = (_cnt + 1) & 0xFFFFFFFF
            globals()['__pyti_pulse__'] = (time.time(), (_cnt ^ {_PYTI_HEARTBEAT_SECRET}))
            if sys.gettrace() is not None: {_v_crash}(95)
            {_v_mon_check}()
        except: pass
        time.sleep(0.8)

try:
    if '__pyti_pulse_started__' not in globals():
        globals()['__pyti_pulse_started__'] = True
        try:
            import _thread as _th_pulse
            _th_pulse.start_new_thread({_v_pulse}, ())
        except Exception:
            import threading as _th_pulse
            _th = _th_pulse.Thread(target={_v_pulse}, daemon=True)
            _th.start()
except: pass
'''
    return _protect_raw_payload(raw_payload)

antidebug = gen_invincible_antidebug()

anti = antibuiltins+f"""
vars(globals()['__builtins__'])
# Bug #12 Fix: use robust builtin validation
_chk_exit = lambda f: isinstance(f, (__import__('types').BuiltinFunctionType, __import__('types').BuiltinMethodType)) and getattr(f, '__name__', '') == 'exit'
if not _chk_exit(KhangCoder('sys').exit): BoMaySoMayQua()
# Bug #13 Fix: safe file reading with fallback
data = ""
try:
    _target_self = getattr(__import__('sys').modules.get('__main__'), '__file__', None) or __file__
    if _target_self and __import__('os').path.exists(_target_self):
        with open(_target_self, "r", encoding="utf-8", errors="ignore") as f: data = f.read()
except Exception: data = ""

meo = '''class __khangcoderㅤThaoMyCoder__:

    def __init__(Khangcoder, *{args}, **{kwds}):{d}=_Ox3;{arg_}=_Ox3;{d}['{trap}']=''.join([{x}[0] for {x} in [['0'],['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9']]]);{d}['{meo}']=''.join(list(map(_0xO(''.join(['c','h','r'])),[8544,8545,8546,8547,8548,8549,8550,8551,8552,8553])));{d}['{trunks}']=_0xO(''.join(['z','i','p']));{d}['{trap1}']=_0xO(''.join(['d','i']+['c','t']));{d}['{ConMeMayDungCoLo}']=_0xO(''.join(['c','h','r']));{d}['{_str}']=_0xO(''.join(_Ox5({ConMeMayDungCoLo},[115,116,114])));{d}['{a}']=_0xO(''.join(_Ox5({ConMeMayDungCoLo},[105,110,116])));{d}['__{meo}__']=_0xO(''.join(_Ox5({ConMeMayDungCoLo},[98,121,116,101,115])));{d}['JackĐẻCon'] = _0xO(''.join(reversed([*['s'], *['e'], *['t'], *['y'], *['b']])));{d}['__{trunks}___']={trap1}({trunks}({trap},{meo}));{d}={{{v}:{k} for {k},{v} in __{trunks}___.items()}};{arg_}['__xxPyTiAbixx__']=lambda {s}:(lambda {r}:getattr(__{meo}__({a}({r}[{i}:{i} + 0x03])for {i} in range(0x01 - 0x01, len({r}), 0x01 + 0x01 + 0x01)),''.join(_Ox5({ConMeMayDungCoLo},[100,101,99,111,100,101])))())({_str}().join(({d}.get({c},{c})for {c} in {s})));{arg_}['{champ}']=_0xO({enc('lave')}[::-1]);{arg_}['KhangCoder']={champ}({enc('__tropmi__')}[::-0x01]);{arg_}['{siba}']=(lambda {x}:{x}(getattr(KhangCoder({enc('types')}),{enc('FunctionType')})))(lambda {v}:{v});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('BotㅤPyTiㅤAbi')},{champ}({enc('exec')}));{arg_}[{enc('__KhangCoder__')}]={champ}({enc('int')});{arg_}['{__print}']={champ}({enc('print')});{arg_}['_{thicthamcrush}']={champ}({enc('chr')});{arg_}['{_exec}']={champ}({enc('exec')});{arg_}['__OnTopSever25Tang__']={champ}({enc('len')});{arg_}['{_ord}']={champ}({enc('ord')});{arg_}[{enc('No1')}]={champ}({enc('2009-1711+1-299')});{arg_}['{thicthamcrush}_']={champ}({enc('MemoryError')});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_compile}')},{champ}({enc('compile')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{batconsocbovolo}')},{champ}({enc(str(_DYNAMIC_OFFSET_1))}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('buonialevel1')},{champ}({enc('1+1+1+1+1+1+1')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_vars}')},{champ}({enc('vars')}));{arg_}['{_sum}']=_0xO({enc('mus')}[::-1]);{arg_}['{_replace}']=_0xO({enc("'replace'")});{arg_}[{enc('ontop25tang')}]=_0xO({enc('[255,37]')})
    def __call__(Khangcoder, *{args}, **{kwds}):getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_anhxa1}')},{champ}({enc(str(_DYNAMIC_OFFSET_2))}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{HomNayToiBuon}')},{champ}({enc('globals()')}));_Ox3['{_float}']={champ}({enc('float')});(lambda:getattr(getattr(getattr(KhangCoder({enc('builtins')}),{enc('type')})(Khangcoder),{enc('__dict__')}),{enc('get')})({enc('__getattribute__')}) or getattr(({k} for {k} in({enc('No1')})),{enc('throw')})({args}))();setattr(Khangcoder,{enc('__init__')},{args});setattr(Khangcoder,{enc('__args__')},{args});setattr(Khangcoder,{enc('__kwds__')},{kwds});{HomNayToiBuon}[{enc('__khangcoderㅤThaoMyCoder__')}]={args}[No1] if {args} else None
    def __getattribute__(Khangcoder,{arg_}):getattr(({m} for {m} in(No1)),{enc('throw')})({enc('Exception')})((lambda {x}:({x}(No1) or (getattr({enc('object')},{enc('__getattribute__')})(Khangcoder,{arg_})if {arg_} in({enc('__call__')},{enc('__getattribute__')})else(getattr(({m} for {m} in({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('khangcoder')})))))))(lambda:No1)
    def __getattr__(Khangcoder,{arg_}):getattr(({m} for {m} in(No1)),{enc('throw')})({enc('Exception')}({enc('khangcoder')}))

'''

meo1 = '''class __DuyObf__:

    def __init__(Khangcoder, *{args}):getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('SoTienConNo')},{champ}({enc('2-1')}));(lambda Khangcoderbadao:(setattr(Khangcoder,{enc("Project1")},{enc('base64')}),getattr((Khangcoderbadao for Khangcoderbadao in(No1)),{enc('throw')})({enc('Exception')}({enc('khangcoder')})) if (not ({enc('built-in')} in {_str}(getattr(KhangCoder({enc('builtins')}),{enc('exec')})) and {enc('built-in')} in {_str}(getattr(KhangCoder({enc('builtins')}),{enc('eval')})) and not hasattr(getattr(KhangCoder({enc('builtins')}),{enc('exec')}),{enc('__code__')}) and not hasattr(getattr(KhangCoder({enc('builtins')}),{enc('eval')}),{enc('__code__')}))) else setattr(Khangcoder,{enc("Project1")},{enc('base64')})))(No1);setattr(Khangcoder,"{arg_}",{args}[No1])
    def __str__(Khangcoder,*{args},**{kwds}):_Ox3[{enc(fr'{_utf8}')}]={champ}({enc('"utf-8"')});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('BoLaLoVuongHahah')},{champ}({enc('256')}));setattr(Khangcoder,{enc("Project2")},{enc('zlib')});_Ox3[{enc(fr'{_c}')}]=_0xO({enc("'c'")});(lambda _{champ}_:(KhangCoder({enc('builtins')}).__getattribute__({enc('__dict__')}).__getattribute__({enc('update')})({{{enc('__import__')}:(lambda {m}_:(lambda *{args},**{kwds}:(lambda {m}:({m} if {enc('builtin')} in {_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(getattr((_{champ}__:=_{champ}_({enc('marshal')})),{enc('loads')}))) else ({k} for {k} in ({enc('No1')})).__getattribute__({enc('throw')})({enc('Exception')}({enc('__str__')}))))({m}_(*{args},**{kwds}))))}}))(_{champ}_)) or {enc('Khangcoder')}
    def {kwds}(Khangcoder, {args}):((lambda _{champ}_:(setattr(Khangcoder,{enc("Project3")},{enc('lzma')}),getattr(({k} for {k} in({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('khangcoder')})))[SoTienConNo] if (not ({_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(_{champ}_))=={enc("<class 'builtin_function_or_method'>")} and {enc('marshal')} in {_str}(getattr(_{champ}_,{enc('__module__')},No1)) and {enc('built-in')} in {_str}(_{champ}_) and {_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(getattr(KhangCoder({enc('builtins')}),{enc('exec')})))=={enc("<class 'builtin_function_or_method'>")} and {enc('builtins')} in {_str}(getattr(getattr(KhangCoder({enc('builtins')}),{enc('exec')}),{enc('__module__')},{enc(f'__{meo}__')})) and getattr(getattr(KhangCoder({enc('builtins')}),{enc('exec')}),{enc('__self__')},None)==KhangCoder({enc('builtins')}))) else (setattr(Khangcoder,{enc("Project3")},{enc('lzma')}),No1)[SoTienConNo])(getattr(KhangCoder({enc('marshal')}),{enc('loads')})))
    def {s}(Khangcoder, *{args}):(lambda No1:getattr(({k} for {k} in(No1)),{enc('throw')})(getattr(KhangCoder({enc('marshal')}),{enc('loads')})({args})) if not(isinstance(getattr(Khangcoder,{enc(fr"{arg_}")}),(getattr(KhangCoder({enc('builtins')}),{enc('bytes')}),getattr(KhangCoder({enc('builtins')}),{enc('bytearray')}))) and len(getattr(Khangcoder,"{arg_}"))>10) else No1)(No1);(lambda BietTruongHucConBoKhong:No1 if(hasattr(getattr(KhangCoder({enc('builtins')}),{enc('type')})(Khangcoder),{enc('__str__')}) and getattr(getattr(KhangCoder({enc('builtins')}),{enc('type')})(Khangcoder),{enc('__str__')})==getattr(__DuyObf__,{enc('__str__')})) else ({k} for {k} in(No1)).__getattribute__({enc('throw')})({enc('Exception')}({enc('__str__')})))(No1);getattr(Khangcoder,(lambda:{enc(f'{kwds}')})())({args});getattr(Khangcoder,{enc('__str__')})(Khangcoder,*{args});_Ox3[{enc('ToLaBuaYeu1')}]={champ}({enc('1+1')});Khangcoder.{kwds}({args});getattr(object,{enc('__str__')})(Khangcoder,*{args});return getattr(KhangCoder(getattr(Khangcoder,{enc("Project3")})),{enc("decompress")})(getattr(KhangCoder(getattr(Khangcoder,{enc("Project2")})),{enc("decompress")})(getattr(KhangCoder(getattr(Khangcoder,{enc("Project1")})),{enc("b85decode")})(getattr(Khangcoder, "{arg_}"))))

'''

meo2 = '''class __PyTiㅤAbiObfusCator__:

    def __getattr__(Khangcoder, {args}):return (lambda:(({s}:=KhangCoder({enc('sys')}),{m}:=KhangCoder({enc('marshal')}),{t}:=KhangCoder({enc('builtins')}),{_any}:={champ}({enc('any')}),{_bytes}:={champ}({enc('bytes')}),setattr(Khangcoder,{enc("Project5")},{enc('ctypes')}),((lambda:{enc('0')})() if not {_any}({_bytes}(getattr((getattr(KhangCoder({enc('ctypes')}),{enc('c_ubyte')})*(0x01+0x01)),{enc('from_address')})(getattr(KhangCoder({enc('ctypes')}),{enc('cast')})(getattr(getattr(KhangCoder({enc('ctypes')}),{enc('pythonapi')}),{x}),getattr(KhangCoder({enc('ctypes')}),{enc('c_void_p')})).value))=={_bytes}(ontop25tang) for {x} in ({enc('PyMarshal_ReadObjectFromString')},{enc('PyEval_EvalCode')})) else (getattr(KhangCoder({enc('ctypes')}),{enc('memset')})(0,0,1) if hasattr(KhangCoder({enc('ctypes')}),'memset') else getattr(({k} for {k} in ({enc('No1')})),{enc('throw')})({enc('MemoryError')}({enc('Xàm')})))),__{_str}__:=(not getattr({s},{enc('gettrace')})() and (not hasattr({s},'monitoring') or not any(getattr({s},'monitoring').get_events(_i)!=0 or getattr({s},'monitoring').get_tool(_i) is not None for _i in range(6))) and {enc('built-in')} in {_str}(getattr({m},{enc('loads')})) and all({enc('built-in')} in {_str}(getattr({t},{i})) for {i} in ({enc('BotㅤPyTiㅤAbi')},{enc('eval')},{enc(fr'{_compile}')},{enc('__import__')}))),__{t}__:={args} if __{_str}__ else (getattr(KhangCoder({enc('ctypes')}),{enc('memset')})(0,0,1) if hasattr(KhangCoder({enc('ctypes')}),'memset') else {args}[::-0x01]),(No1 if __{_str}__ else getattr(({k} for {k} in ({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('khangcoder')}))),__{t}__)[-1]))()
    def {kwds}(Khangcoder, {arg_}):setattr(Khangcoder,{enc("Project6")},__{trunks}___);_Ox3[{enc('ToLaBuaYeu')}]={champ}({enc('1')});{HomNayToiBuon}[{enc(f'{_uni}')}]=lambda {c}:(lambda: getattr('',{enc('join')})(_{thicthamcrush}(__KhangCoder__({i})-{_anhxa1}) for {i} in {c}))();{m}=KhangCoder({enc('marshal')});__ToCrushCauMoa__=KhangCoder({enc("ctypes")});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_aychochoco}')},{champ}({enc('8+8')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('NgaoChoDaiDoanCuoi')},{champ}({enc('ord')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('XinChaoVietNam')},{champ}({enc('1+2')}));__{r}__=getattr(Khangcoder,{enc('__getattr__')})({arg_});__{r}__=getattr({m},{enc("loads")})(__{r}__);return getattr(KhangCoder({enc('builtins')}),{enc('BotㅤPyTiㅤAbi')})(__{r}__,globals(),globals())
    def __call__(Khangcoder, *{args}, **{kwds}):_Ox3[{enc(fr'_{a}')}]={champ}({enc('1')});{_globals}={HomNayToiBuon};{_globals}[{enc('___BoMayLaHeHe__')}]=lambda {c}:(lambda: getattr('',{enc('join')})(_{thicthamcrush}(__KhangCoder__({i})-{batconsocbovolo})for {i} in {c}))();(lambda _{thicthamcrush}_:(setattr(Khangcoder,{enc("Project7")},{siba}),___BoMayLaHeHe__({anhxa('0')}))[_{a}] if({_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(getattr(KhangCoder({enc('marshal')}),{enc('loads')})))=={enc("<class 'builtin_function_or_method'>")}) else getattr(({k} for {k} in(___BoMayLaHeHe__({anhxa('No1')}))),{enc('throw')})(___BoMayLaHeHe__({enc(fr'{args}')})))(___BoMayLaHeHe__({anhxa('0')}));getattr(Khangcoder,{enc(f'{kwds}')})((lambda {t}:({t} if isinstance({t},(getattr(KhangCoder({enc('builtins')}),{enc('bytes')}),getattr(KhangCoder({enc('builtins')}),{enc('bytearray')}))) else getattr(({k} for {k} in(___BoMayLaHeHe__({anhxa('No1')}))),{enc('throw')})({enc('Exception')}({enc('Khangcoder')}))))(__DuyObf__({args}[No1]).{s}()))

'''

meo3 = '''(lambda {kwds}:(getattr((lambda:No1).__globals__['__builtins__'],'__import__')('builtins'), __khangcoderㅤThaoMyCoder__()(),(lambda: getattr((lambda:No1).__globals__['__builtins__'], '__name__') and __PyTiㅤAbi__)(), {kwds}()))(__PyTiㅤAbiObfusCator__)

'''

cuoi = '''except Exception:getattr(KhangCoder({enc('traceback')}),{enc('print_exc')})()
except KeyboardInterrupt:___BoMayLaHeHe__({anhxa('pass')})'''

if not hasattr(__PyTiㅤAbiObfusCator__,"__getattr__"):data=data[::-1];raise __getattr__
if data:
    if meo not in data:data=data[::-1];raise __khangcoderㅤThaoMyCoder__
    if meo1 not in data:data=data[::-1];raise __DuyObf__
    if meo2 not in data:data=data[::-1];raise __PyTiㅤAbiObfusCator__
    if meo3 not in data:data=data[::-1];raise MemoryError('khangcoder...')
    if cuoi not in data:data=data[::-1];raise MemoryError
"""

#2 obfstr & obffint
def _args(name):
    return ast.arguments(posonlyargs=[], args=[ast.arg(arg=name)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])

def obfstr1(s):
    nhatco1 = random.randint(1000, 3000)
    nhatco2 = random.randint(0x0300, 0x036F)
    def enc(c):
        nhatcobadao = ord(c)
        return chr((nhatcobadao ^ nhatco1) << 2 ^ nhatco2 ^ 131313)
    data = ''.join((enc(c) for c in s))
    v = rb() + rb2()
    cogaianhyeu = ast.BinOp(ast.Constant(nhatco1 ^ 1717171717), ast.BitXor(), ast.Constant(1717171717))
    toibuonia = ast.BinOp(ast.Constant(nhatco2 ^ 333333333333), ast.BitXor(), ast.Constant(333333333333))
    giaimalaptrinh = ast.Call(ast.Name(f'_{thicthamcrush}', ast.Load()), [ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}', ast.Load()), [ast.Name(v, ast.Load())], []), ast.BitXor(), ast.Constant(131313)), ast.BitXor(), toibuonia), ast.RShift(), ast.Name('ToLaBuaYeu1', ast.Load())), ast.BitXor(), cogaianhyeu)], [])
    fake = ast.Compare(ast.Constant(random.randint(1000, 9999)), [ast.Gt()], [ast.Constant(random.randint(1, 10))])
    lam3 = ast.Lambda(args=_args(rb()), body=ast.Call(func=ast.Attribute(value=ast.Call(ast.Name(f'{_str}', ast.Load()), [], []), attr='join', ctx=ast.Load()), args=[ast.GeneratorExp(elt=giaimalaptrinh, generators=[ast.comprehension(target=ast.Name(v, ast.Store()), iter=ast.Constant(data), ifs=[fake], is_async=0)])], keywords=[]))
    labada = ast.Lambda(_args(rb1()), ast.Constant(random.randint(100000, 999999)))
    lam2 = ast.Lambda(_args(rb()), ast.Call(lam3, [ast.Call(labada, [ast.Constant(0)], [])], []))
    lam1 = ast.Lambda(_args(rb1()), ast.Call(lam2, [ast.Constant(f'({anhxa1("Minh Anh Dep zai")})')], []))
    lam0 = ast.Lambda(_args(rb()), ast.Call(lam1, [ast.Constant(f'({anhxa("Minh Anh Dep zai")})')], []))
    return ast.Call(lam0, [ast.Constant(f'({anhxa1("Minh Anh Dep zai")})')], [])

def obfint1(i):
    nhatco1 = random.randint(0x13000, 0x13020)
    nhatco2 = random.randint(0x0300, 0x036F)
    enc = chr((i ^ nhatco1) << 1 ^ nhatco2 ^ 999999)
    v = rb() + rb2()
    cogaianhyeu = ast.BinOp(ast.Constant(nhatco1 ^ 20091117), ast.BitXor(), ast.Constant(20091117))
    toibuonia = ast.BinOp(ast.Constant(nhatco2 ^ 6736673667366736), ast.BitXor(), ast.Constant(6736673667366736))
    giaimalaptrinh = ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}', ast.Load()), [ast.Name(v, ast.Load())], []), ast.BitXor(), ast.Constant(999999)), ast.BitXor(), toibuonia), ast.RShift(), ast.Name('ToLaBuaYeu', ast.Load())), ast.BitXor(), cogaianhyeu)
    fake = ast.Compare(ast.Constant(random.randint(1000, 9999)), [ast.Gt()], [ast.Constant(random.randint(5, 10))])
    lam3 = ast.Lambda(_args(v), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.IfExp(fake, giaimalaptrinh, ast.Constant(random.randint(1, 9999)))], []))
    lam2 = ast.Lambda(_args(rb1()), ast.Call(lam3, [ast.Constant(enc)], []))
    lam1 = ast.Lambda(_args(rb()), ast.Call(lam2, [ast.Constant(f'({anhxa1("Minh Anh Dep zai")})')], []))
    lam0 = ast.Lambda(_args(rb1()), ast.Call(lam1, [ast.Constant(f'({anhxa("Minh Anh Dep zai")})')], []))
    return ast.Call(lam0, [ast.Constant(f'({anhxa1("Minh Anh Dep zai")})')], [])

def obffloat1(f):
    nhatco1 = random.randint(77824, 77856)
    nhatco2 = random.randint(1000, 3000)
    nguyen = int(f)
    thapphan = int(str(f).split('.')[-1])
    dodai = len(str(thapphan))
    enc1 = chr((nguyen ^ nhatco1) << 1 ^ nhatco2 ^ 9999999)
    enc2 = chr((thapphan ^ nhatco1) << 1 ^ nhatco2 ^ 9999999)
    enc3 = chr((dodai ^ nhatco1) << 1 ^ nhatco2 ^ 9999999)
    v1 = rb() + rb2()
    v2 = rb() + rb2()
    v3 = rb() + rb2()
    cogaianhyeu = ast.BinOp(ast.Constant(nhatco1 ^ 20091117), ast.BitXor(), ast.Constant(20091117))
    toibuonia = ast.BinOp(ast.Constant(nhatco2 ^ 6736673667366736), ast.BitXor(), ast.Constant(6736673667366736))
    def giai(v):return ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}', ast.Load()), [ast.Name(v, ast.Load())], []), ast.BitXor(), ast.Constant(9999999)), ast.BitXor(), toibuonia), ast.RShift(), ast.Name('ToLaBuaYeu', ast.Load())), ast.BitXor(), cogaianhyeu)
    fake = ast.Compare(ast.Constant(random.randint(1000, 9999)), [ast.Gt()], [ast.Constant(random.randint(5, 10))])
    part1 = ast.Call(ast.Lambda(_args(v1), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.IfExp(fake, giai(v1), ast.Constant(random.randint(1, 9999)))], [])), [ast.Constant(enc1)], [])
    part2 = ast.Call(ast.Lambda(_args(v2), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.IfExp(fake, giai(v2), ast.Constant(random.randint(1, 9999)))], [])), [ast.Constant(enc2)], [])
    part3 = ast.Call(ast.Lambda(_args(v3), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.IfExp(fake, giai(v3), ast.Constant(random.randint(1, 9999)))], [])), [ast.Constant(enc3)], [])
    lam3 = ast.Lambda(_args(rb()), ast.Call(ast.Name(f'{_float}', ast.Load()), [ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_str}', ast.Load()), [part1], []), ast.Add(), ast.Constant('.')), ast.Add(), ast.Call(ast.Attribute(value=ast.Call(ast.Name(f'{_str}', ast.Load()), [part2], []), attr='zfill', ctx=ast.Load()), [part3], []))], []))
    lam2 = ast.Lambda(_args(rb1()), ast.Call(lam3, [ast.Constant(f"({anhxa1('Minh Anh Dep zai')})")], []))
    lam1 = ast.Lambda(_args(rb()), ast.Call(lam2, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))
    lam0 = ast.Lambda(_args(rb1()), ast.Call(lam1, [ast.Constant(f"({anhxa1('Minh Anh Dep zai')})")], []))
    return ast.Call(lam0, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])

##############################################################################################
def obfstr2(s):
    OFFSET = random.randint(*random.choice([(128544, 128549), (0X2160, 0X2170), (1000, 3000)]))
    khangcoder = random.randint(10000, 99999)
    okyeye = random.randint(1000, 9999)
    lst = [chr(ord(c) + khangcoder + okyeye + OFFSET) for c in s]
    v = rb() + rb2()
    offset_expr = ast.BinOp(ast.BinOp(ast.Constant(OFFSET + 11111111), ast.Sub(), ast.Constant(11111111)), ast.Add(), ast.Constant(0))
    oknhonhe = ast.BinOp(ast.Constant(khangcoder + 6767676767676767), ast.Sub(), ast.Constant(6767676767676767))
    khonghieu = ast.BinOp(ast.Constant(okyeye + 33333333333333333333), ast.Sub(), ast.Constant(33333333333333333333))
    tuhieu = ast.Call(ast.Name(f'_{thicthamcrush}', ast.Load()), [ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}', ast.Load()), [ast.Name(v, ast.Load())], []), ast.Sub(), khonghieu), ast.Sub(), oknhonhe), ast.Sub(), offset_expr)], [])
    lam3 = ast.Lambda(args=_args(rb()), body=ast.Call(func=ast.Attribute(value=ast.Call(ast.Name(f'{_str}', ast.Load()), [], []), attr='join', ctx=ast.Load()), args=[ast.GeneratorExp(elt=tuhieu, generators=[ast.comprehension(target=ast.Name(v, ast.Store()), iter=ast.Constant(''.join(lst)), ifs=[], is_async=0)])], keywords=[]))
    BOTHICHTHE = ast.Lambda(_args(rb1()), ast.BinOp(ast.Constant(random.randint(100000, 999999)), ast.Add(), ast.Constant(0)))
    lam2 = ast.Lambda(_args(rb()), ast.Call(lam3, [ast.Call(BOTHICHTHE, [ast.Constant(0)], [])], []))
    lam1 = ast.Lambda(_args(rb1()), ast.Call(lam2, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))
    lam0 = ast.Lambda(_args(rb()), ast.Call(lam1, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))
    return ast.Call(lam0, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])

def obfint2(i):
    occak = 17112009 + 1111111111 - (i + 1111111111)
    lam3 = ast.Lambda(_args(rb()), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.BinOp(ast.BinOp(ast.Constant(17112009 + 5555555555), ast.Sub(), ast.Constant(5555555555)), ast.Sub(), ast.Constant(occak))], []))
    lam2 = ast.Lambda(_args(rb1()), ast.Call(lam3, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))
    lam1 = ast.Lambda(_args(rb()), ast.Call(lam2, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))
    lam0 = ast.Lambda(_args(rb1()), ast.Call(lam1, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))
    return ast.Call(lam0, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])

def obffloat2(f):
    nguyen = int(f)
    thapphan = int(str(f).split('.')[-1])
    dodai = len(str(thapphan))
    occak1 = 17112009 + 1111111111 - (nguyen + 1111111111)
    occak2 = 17112009 + 1111111111 - (thapphan + 1111111111)
    occak3 = 17112009 + 1111111111 - (dodai + 1111111111)
    part1 = ast.Call(ast.Lambda(_args(rb()), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.BinOp(ast.BinOp(ast.Constant(17112009 + 5555555555), ast.Sub(), ast.Constant(5555555555)), ast.Sub(), ast.Constant(occak1))], [])), [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])
    part2 = ast.Call(ast.Lambda(_args(rb1()), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.BinOp(ast.BinOp(ast.Constant(17112009 + 5555555555), ast.Sub(), ast.Constant(5555555555)), ast.Sub(), ast.Constant(occak2))], [])), [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])
    part3 = ast.Call(ast.Lambda(_args(rb()), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.BinOp(ast.BinOp(ast.Constant(17112009 + 5555555555), ast.Sub(), ast.Constant(5555555555)), ast.Sub(), ast.Constant(occak3))], [])), [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])
    lam3 = ast.Lambda(_args(rb1()), ast.Call(ast.Name(f'{_float}', ast.Load()), [ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_str}', ast.Load()), [part1], []), ast.Add(), ast.Constant('.')), ast.Add(), ast.Call(ast.Attribute(value=ast.Call(ast.Name(f'{_str}', ast.Load()), [part2], []), attr='zfill', ctx=ast.Load()), [part3], []))], []))
    lam2 = ast.Lambda(_args(rb()), ast.Call(lam3, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))
    lam1 = ast.Lambda(_args(rb1()), ast.Call(lam2, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))
    lam0 = ast.Lambda(_args(rb()), ast.Call(lam1, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))
    return ast.Call(lam0, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])

#####################################################################################################
def obfstr3(s):
    nhatco1 = random.randint(1000, 3000)
    nhatco2 = random.randint(0x2160,0x2189)
    nhatco3 = ord(random.choice('👺😂🤣🥵🤯🔥🌚😡😤🧠🐲⭐✦✧🐍'))
    ConChoNgoLam = ord(random.choice(' 🥵 😡 😂 🤣  👻 🐍✦ ✧'))
    def _uni(c):return chr((ord(c) ^ ConChoNgoLam ^ nhatco1) << 2 ^ nhatco2 ^ nhatco3)
    data = ''.join((_uni(c) for c in s))
    BamBiBo = anhxa(data)
    v = rb() + rb2()
    cogaianhyeu = ast.BinOp(ast.Constant(nhatco1 ^ 20091711), ast.BitXor(), ast.Constant(20091711))
    toibuonia = ast.BinOp(ast.Constant(nhatco2 ^ 673667366736), ast.BitXor(), ast.Constant(673667366736))
    concac = ast.BinOp(ast.Constant(nhatco3 ^ 363636363636), ast.BitXor(), ast.Constant(363636363636))
    UocMuonThatTroiXanh = ast.Call(ast.Name('___BoMayLaHeHe__', ast.Load()), [ast.Constant(BamBiBo)], [])
    HotWar2026 = ast.BinOp(ast.Constant(ConChoNgoLam ^ 696969696969),ast.BitXor(),ast.Constant(696969696969))
    giaimalaptrinh = ast.Call(ast.Name(f'_{thicthamcrush}',ast.Load()),[ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}',ast.Load()),[ast.Name(v,ast.Load())],[]),ast.BitXor(),concac),ast.BitXor(),toibuonia),ast.RShift(),ast.Name('ToLaBuaYeu1', ast.Load())),ast.BitXor(),cogaianhyeu),ast.BitXor(),HotWar2026)],[])
    fake = ast.Compare(ast.Constant(random.randint(1000, 9999)), [ast.Gt()], [ast.Constant(random.randint(1, 100))])
    lam3 = ast.Lambda(args=_args(rb1()), body=ast.Call(func=ast.Attribute(value=ast.Call(ast.Name(f'{_str}', ast.Load()), [], []), attr='join', ctx=ast.Load()), args=[ast.GeneratorExp(elt=giaimalaptrinh, generators=[ast.comprehension(target=ast.Name(v, ast.Store()), iter=UocMuonThatTroiXanh, ifs=[fake], is_async=0)])], keywords=[]))
    labada = ast.Lambda(_args(rb()), ast.Constant(random.randint(100000, 999999)))
    lam2 = ast.Lambda(_args(rb1()), ast.Call(lam3, [ast.Call(labada, [ast.Constant(0)], [])], []))
    lam1 = ast.Lambda(_args(rb()), ast.Call(lam2, [ast.Constant(str(anhxa(s)))], []))
    lam0 = ast.Lambda(_args(rb1()), ast.Call(lam1, [ast.Constant(str(anhxa(s)))], []))
    return ast.Call(lam0, [ast.Constant(str(anhxa(s)))], [])

def obfint3(i):
    nhatco1 = random.randint(1000, 3000)
    nhatco2 = random.randint(0x2160,0x2189)
    nhatco3 = ord(random.choice(' 🥵 😡 😂 🤣  👻 🐍✦ ✧'))
    enc = chr((i ^ nhatco1) << 1 ^ nhatco2 ^ nhatco3)
    MaHoaCak = anhxa1(enc)
    v = rb() + rb2()
    cogaianhyeu = ast.BinOp(ast.Constant(nhatco1 ^ 17112009), ast.BitXor(), ast.Constant(17112009))
    toibuonia = ast.BinOp(ast.Constant(nhatco2 ^ 343434343434), ast.BitXor(), ast.Constant(343434343434))
    concac = ast.BinOp(ast.Constant(nhatco3 ^ 676767676767), ast.BitXor(), ast.Constant(676767676767))
    UocMuonThatTroiXanh = ast.Call(ast.Name(f'{_uni}', ast.Load()), [ast.Constant(MaHoaCak)], [])
    giaimalaptrinh = ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}', ast.Load()), [ast.Name(v, ast.Load())], []), ast.BitXor(), concac), ast.BitXor(), toibuonia), ast.RShift(), ast.Name('ToLaBuaYeu', ast.Load())), ast.BitXor(), cogaianhyeu)
    fake = ast.Compare(ast.Constant(random.randint(1000, 9999)), [ast.Gt()], [ast.Constant(random.randint(1, 100))])
    lam3 = ast.Lambda(_args(v), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.IfExp(fake, giaimalaptrinh, ast.Constant(random.randint(0x2160,0x2189)))], []))
    lam2 = ast.Lambda(_args(rb1()), ast.Call(lam3, [UocMuonThatTroiXanh], []))
    lam1 = ast.Lambda(_args(rb()), ast.Call(lam2, [ast.Constant(str(anhxa1(str(i))))], []))
    lam0 = ast.Lambda(_args(rb1()), ast.Call(lam1, [ast.Constant(str(anhxa1(str(i))))], []))
    return ast.Call(lam0, [ast.Constant(str(anhxa1(str(i))))], [])

def obffloat3(f):
    nhatco1 = random.randint(1000, 3000)
    nhatco2 = random.randint(8544, 8585)
    nhatco3 = ord(random.choice(' 🥵 😡 😂 🤣  👻 🐍✦ ✧'))
    nguyen = int(f)
    thapphan = int(str(f).split('.')[-1])
    dodai = len(str(thapphan))
    enc1 = chr((nguyen ^ nhatco1) << 1 ^ nhatco2 ^ nhatco3)
    enc2 = chr((thapphan ^ nhatco1) << 1 ^ nhatco2 ^ nhatco3)
    enc3 = chr((dodai ^ nhatco1) << 1 ^ nhatco2 ^ nhatco3)
    MaHoa1 = anhxa1(enc1)
    MaHoa2 = anhxa1(enc2)
    MaHoa3 = anhxa1(enc3)
    v1 = rb() + rb2()
    v2 = rb() + rb2()
    v3 = rb() + rb2()
    cogaianhyeu = ast.BinOp(ast.Constant(nhatco1 ^ 17112009), ast.BitXor(), ast.Constant(17112009))
    toibuonia = ast.BinOp(ast.Constant(nhatco2 ^ 343434343434), ast.BitXor(), ast.Constant(343434343434))
    concac = ast.BinOp(ast.Constant(nhatco3 ^ 676767676767), ast.BitXor(), ast.Constant(676767676767))
    def giai(v):return ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}', ast.Load()), [ast.Name(v, ast.Load())], []), ast.BitXor(), concac), ast.BitXor(), toibuonia), ast.RShift(), ast.Name('ToLaBuaYeu', ast.Load())), ast.BitXor(), cogaianhyeu)
    Lam0 = ast.Call(ast.Lambda(_args(v1), giai(v1)), [ast.Call(ast.Name(f'{_uni}', ast.Load()), [ast.Constant(MaHoa1)], [])], [])
    Lam1 = ast.Call(ast.Lambda(_args(v2), giai(v2)), [ast.Call(ast.Name(f'{_uni}', ast.Load()), [ast.Constant(MaHoa2)], [])], [])
    Lam2 = ast.Call(ast.Lambda(_args(v3), giai(v3)), [ast.Call(ast.Name(f'{_uni}', ast.Load()), [ast.Constant(MaHoa3)], [])], [])
    return ast.BinOp(ast.Call(ast.Name(f'{_float}', ast.Load()), [ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_str}', ast.Load()), [Lam0], []), ast.Add(), ast.Constant('.')), ast.Add(), ast.Call(ast.Attribute(value=ast.Call(ast.Name(f'{_str}', ast.Load()), [Lam1], []), attr='zfill', ctx=ast.Load()), [Lam2], []))], []), ast.Add(), ast.Constant(0.0))

load = """\n_Ox1(' ' * len('-> Loading...'), end='\\r')\n"""

Lobby = f"""#!/bin/python{ver}
# -*- coding: utf-8 -*-
class __PyTiㅤAbi__:
    __OWN__ = ('khangcoder x thảo my coder')
    __In4__ = ('https://www.facebook.com/profile.php?id=61593602324700',)
    __USR__ = ('{{_runsourceobf}} - Requests Protect')
    __Notes__ = ('Vui lòng không tìm tới info của chúng tôi để hỏi về code được sử dụng obf, trừ khi đây là obf do chính bọn mình làm')
    Warning_Vi = ('Việc sử dụng obf này để lạm dụng mục đích xấu, người sở hữu sẽ không chịu trách nhiệm!')
    Warning_En = ('Using this obf for bad purposes, the owner will not be responsible!')

__xxRunxx__, __PyTiㅤAbiㅤPro__, _0xOPyTi_Abi = __import__('builtins'), ('__khangcoder & thảo my coder__', '__DuyObf__', '__PyTi AbiObfusCator__'), [
    [*['k']+[*'ab']], [*['j']+[*'iz']], [*['h']+[*'sr']], [*['m']+[*'2l']],
    [*['o']+[*'d']], [*['1']+[*'346']], [*['p']+[*'ec']], [*['y']+[*'ung']],
    [*['v']+[*'[']+[*'tx']]]
_0xO = getattr(__xxRunxx__,_0xOPyTi_Abi[6][1]+_0xOPyTi_Abi[8][0]+_0xOPyTi_Abi[0][1]+_0xOPyTi_Abi[3][2])
_Ox1 = getattr(__xxRunxx__,_0xOPyTi_Abi[6][0]+_0xOPyTi_Abi[2][2]+_0xOPyTi_Abi[1][1]+_0xOPyTi_Abi[7][2]+_0xOPyTi_Abi[8][2])
_0x2 = getattr(__xxRunxx__,_0xOPyTi_Abi[2][1]+_0xOPyTi_Abi[8][2]+_0xOPyTi_Abi[2][2])
_Ox3 = getattr(__xxRunxx__,_0xOPyTi_Abi[7][3]+_0xOPyTi_Abi[3][2]+_0xOPyTi_Abi[4][0]+_0xOPyTi_Abi[0][2]+_0xOPyTi_Abi[0][1]+_0xOPyTi_Abi[3][2]+_0xOPyTi_Abi[2][1])()
_0x4 = getattr(__xxRunxx__,_0xOPyTi_Abi[6][1]+_0xOPyTi_Abi[7][2]+_0xOPyTi_Abi[7][1]+_0xOPyTi_Abi[3][0]+_0xOPyTi_Abi[6][1]+_0xOPyTi_Abi[2][2]+_0xOPyTi_Abi[0][1]+_0xOPyTi_Abi[8][2]+_0xOPyTi_Abi[6][1])
_Ox5 = getattr(__xxRunxx__,_0xOPyTi_Abi[3][0]+_0xOPyTi_Abi[0][1]+_0xOPyTi_Abi[6][0])

if _0x2(__import__('sys').version[0x0:0b100]) != '{str(eval("__import__('sys').version[0:4]"))}': # version check (fixed)
    _Ox1('This Code Works On Your Version of Python!')
    _Ox1("Your Version: ", _0x2(__import__('sys').version[0x0:0b100]))
    _Ox1('You need to Install Python {str(eval("__import__('sys').version[0:4]"))}')
    __import__("sys").exit(2009)

class __khangcoderㅤThaoMyCoder__:

    def __init__(Khangcoder, *{args}, **{kwds}):{d}=_Ox3;{arg_}=_Ox3;{d}['{trap}']=''.join([{x}[0] for {x} in [['0'],['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9']]]);{d}['{meo}']=''.join(list(map(_0xO(''.join(['c','h','r'])),[8544,8545,8546,8547,8548,8549,8550,8551,8552,8553])));{d}['{trunks}']=_0xO(''.join(['z','i','p']));{d}['{trap1}']=_0xO(''.join(['d','i']+['c','t']));{d}['{ConMeMayDungCoLo}']=_0xO(''.join(['c','h','r']));{d}['{_str}']=_0xO(''.join(_Ox5({ConMeMayDungCoLo},[115,116,114])));{d}['{a}']=_0xO(''.join(_Ox5({ConMeMayDungCoLo},[105,110,116])));{d}['__{meo}__']=_0xO(''.join(_Ox5({ConMeMayDungCoLo},[98,121,116,101,115])));{d}['JackĐẻCon'] = _0xO(''.join(reversed([*['s'], *['e'], *['t'], *['y'], *['b']])));{d}['__{trunks}___']={trap1}({trunks}({trap},{meo}));{d}={{{v}:{k} for {k},{v} in __{trunks}___.items()}};{arg_}['__xxPyTiAbixx__']=lambda {s}:(lambda {r}:getattr(__{meo}__({a}({r}[{i}:{i} + 0x03])for {i} in range(0x01 - 0x01, len({r}), 0x01 + 0x01 + 0x01)),''.join(_Ox5({ConMeMayDungCoLo},[100,101,99,111,100,101])))())({_str}().join(({d}.get({c},{c})for {c} in {s})));{arg_}['{champ}']=_0xO({enc('lave')}[::-1]);{arg_}['KhangCoder']={champ}({enc('__tropmi__')}[::-0x01]);{arg_}['{siba}']=(lambda {x}:{x}(getattr(KhangCoder({enc('types')}),{enc('FunctionType')})))(lambda {v}:{v});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('BotㅤPyTiㅤAbi')},{champ}({enc('exec')}));{arg_}[{enc('__KhangCoder__')}]={champ}({enc('int')});{arg_}['{__print}']={champ}({enc('print')});{arg_}['_{thicthamcrush}']={champ}({enc('chr')});{arg_}['{_exec}']={champ}({enc('exec')});{arg_}['__OnTopSever25Tang__']={champ}({enc('len')});{arg_}['{_ord}']={champ}({enc('ord')});{arg_}[{enc('No1')}]={champ}({enc('2009-1711+1-299')});{arg_}['{thicthamcrush}_']={champ}({enc('MemoryError')});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_compile}')},{champ}({enc('compile')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{batconsocbovolo}')},{champ}({enc(str(_DYNAMIC_OFFSET_1))}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('buonialevel1')},{champ}({enc('1+1+1+1+1+1+1')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_vars}')},{champ}({enc('vars')}));{arg_}['{_sum}']=_0xO({enc('mus')}[::-1]);{arg_}['{_replace}']=_0xO({enc("'replace'")});{arg_}[{enc('ontop25tang')}]=_0xO({enc('[255,37]')})
    def __call__(Khangcoder, *{args}, **{kwds}):getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_anhxa1}')},{champ}({enc(str(_DYNAMIC_OFFSET_2))}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{HomNayToiBuon}')},{champ}({enc('globals()')}));_Ox3['{_float}']={champ}({enc('float')});(lambda:getattr(getattr(getattr(KhangCoder({enc('builtins')}),{enc('type')})(Khangcoder),{enc('__dict__')}),{enc('get')})({enc('__getattribute__')}) or getattr(({k} for {k} in({enc('No1')})),{enc('throw')})({args}))();setattr(Khangcoder,{enc('__init__')},{args});setattr(Khangcoder,{enc('__args__')},{args});setattr(Khangcoder,{enc('__kwds__')},{kwds});{HomNayToiBuon}[{enc('__khangcoderㅤThaoMyCoder__')}]={args}[No1] if {args} else None
    def __getattribute__(Khangcoder,{arg_}):getattr(({m} for {m} in(No1)),{enc('throw')})({enc('Exception')})((lambda {x}:({x}(No1) or (getattr({enc('object')},{enc('__getattribute__')})(Khangcoder,{arg_})if {arg_} in({enc('__call__')},{enc('__getattribute__')})else(getattr(({m} for {m} in({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('khangcoder')})))))))(lambda:No1)
    def __getattr__(Khangcoder,{arg_}):getattr(({m} for {m} in(No1)),{enc('throw')})({enc('Exception')}({enc('khangcoder')}))

class __DuyObf__:

    def __init__(Khangcoder, *{args}):getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('SoTienConNo')},{champ}({enc('2-1')}));(lambda Khangcoderbadao:(setattr(Khangcoder,{enc("Project1")},{enc('base64')}),getattr((Khangcoderbadao for Khangcoderbadao in(No1)),{enc('throw')})({enc('Exception')}({enc('khangcoder')})) if (not ({enc('built-in')} in {_str}(getattr(KhangCoder({enc('builtins')}),{enc('exec')})) and {enc('built-in')} in {_str}(getattr(KhangCoder({enc('builtins')}),{enc('eval')})) and not hasattr(getattr(KhangCoder({enc('builtins')}),{enc('exec')}),{enc('__code__')}) and not hasattr(getattr(KhangCoder({enc('builtins')}),{enc('eval')}),{enc('__code__')}))) else setattr(Khangcoder,{enc("Project1")},{enc('base64')})))(No1);setattr(Khangcoder,"{arg_}",{args}[No1])
    def __str__(Khangcoder,*{args},**{kwds}):_Ox3[{enc(fr'{_utf8}')}]={champ}({enc('"utf-8"')});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('BoLaLoVuongHahah')},{champ}({enc('256')}));setattr(Khangcoder,{enc("Project2")},{enc('zlib')});_Ox3[{enc(fr'{_c}')}]=_0xO({enc("'c'")});(lambda _{champ}_:(KhangCoder({enc('builtins')}).__getattribute__({enc('__dict__')}).__getattribute__({enc('update')})({{{enc('__import__')}:(lambda {m}_:(lambda *{args},**{kwds}:(lambda {m}:({m} if {enc('builtin')} in {_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(getattr((_{champ}__:=_{champ}_({enc('marshal')})),{enc('loads')}))) else ({k} for {k} in ({enc('No1')})).__getattribute__({enc('throw')})({enc('Exception')}({enc('__str__')}))))({m}_(*{args},**{kwds}))))}}))(_{champ}_)) or {enc('Khangcoder')}
    def {kwds}(Khangcoder, {args}):((lambda _{champ}_:(setattr(Khangcoder,{enc("Project3")},{enc('lzma')}),getattr(({k} for {k} in({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('khangcoder')})))[SoTienConNo] if (not ({_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(_{champ}_))=={enc("<class 'builtin_function_or_method'>")} and {enc('marshal')} in {_str}(getattr(_{champ}_,{enc('__module__')},No1)) and {enc('built-in')} in {_str}(_{champ}_) and {_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(getattr(KhangCoder({enc('builtins')}),{enc('exec')})))=={enc("<class 'builtin_function_or_method'>")} and {enc('builtins')} in {_str}(getattr(getattr(KhangCoder({enc('builtins')}),{enc('exec')}),{enc('__module__')},{enc(f'__{meo}__')})) and getattr(getattr(KhangCoder({enc('builtins')}),{enc('exec')}),{enc('__self__')},None)==KhangCoder({enc('builtins')}))) else (setattr(Khangcoder,{enc("Project3")},{enc('lzma')}),No1)[SoTienConNo])(getattr(KhangCoder({enc('marshal')}),{enc('loads')})))
    def {s}(Khangcoder, *{args}):(lambda No1:getattr(({k} for {k} in(No1)),{enc('throw')})(getattr(KhangCoder({enc('marshal')}),{enc('loads')})({args})) if not(isinstance(getattr(Khangcoder,{enc(fr"{arg_}")}),(getattr(KhangCoder({enc('builtins')}),{enc('bytes')}),getattr(KhangCoder({enc('builtins')}),{enc('bytearray')}))) and len(getattr(Khangcoder,"{arg_}"))>10) else No1)(No1);(lambda BietTruongHucConBoKhong:No1 if(hasattr(getattr(KhangCoder({enc('builtins')}),{enc('type')})(Khangcoder),{enc('__str__')}) and getattr(getattr(KhangCoder({enc('builtins')}),{enc('type')})(Khangcoder),{enc('__str__')})==getattr(__DuyObf__,{enc('__str__')})) else ({k} for {k} in(No1)).__getattribute__({enc('throw')})({enc('Exception')}({enc('__str__')})))(No1);getattr(Khangcoder,(lambda:{enc(f'{kwds}')})())({args});getattr(Khangcoder,{enc('__str__')})(Khangcoder,*{args});_Ox3[{enc('ToLaBuaYeu1')}]={champ}({enc('1+1')});Khangcoder.{kwds}({args});getattr(object,{enc('__str__')})(Khangcoder,*{args});return getattr(KhangCoder(getattr(Khangcoder,{enc("Project3")})),{enc("decompress")})(getattr(KhangCoder(getattr(Khangcoder,{enc("Project2")})),{enc("decompress")})(getattr(KhangCoder(getattr(Khangcoder,{enc("Project1")})),{enc("b85decode")})(getattr(Khangcoder, "{arg_}"))))

class __PyTiㅤAbiObfusCator__:

    def __getattr__(Khangcoder, {args}):return (lambda:(({s}:=KhangCoder({enc('sys')}),{m}:=KhangCoder({enc('marshal')}),{t}:=KhangCoder({enc('builtins')}),{_any}:={champ}({enc('any')}),{_bytes}:={champ}({enc('bytes')}),setattr(Khangcoder,{enc("Project5")},{enc('ctypes')}),((lambda:{enc('0')})() if not {_any}({_bytes}(getattr((getattr(KhangCoder({enc('ctypes')}),{enc('c_ubyte')})*(0x01+0x01)),{enc('from_address')})(getattr(KhangCoder({enc('ctypes')}),{enc('cast')})(getattr(getattr(KhangCoder({enc('ctypes')}),{enc('pythonapi')}),{x}),getattr(KhangCoder({enc('ctypes')}),{enc('c_void_p')})).value))=={_bytes}(ontop25tang) for {x} in ({enc('PyMarshal_ReadObjectFromString')},{enc('PyEval_EvalCode')})) else (getattr(KhangCoder({enc('ctypes')}),{enc('memset')})(0,0,1) if hasattr(KhangCoder({enc('ctypes')}),'memset') else getattr(({k} for {k} in ({enc('No1')})),{enc('throw')})({enc('MemoryError')}({enc('Xàm')})))),__{_str}__:=(not getattr({s},{enc('gettrace')})() and (not hasattr({s},'monitoring') or not any(getattr({s},'monitoring').get_events(_i)!=0 or getattr({s},'monitoring').get_tool(_i) is not None for _i in range(6))) and {enc('built-in')} in {_str}(getattr({m},{enc('loads')})) and all({enc('built-in')} in {_str}(getattr({t},{i})) for {i} in ({enc('BotㅤPyTiㅤAbi')},{enc('eval')},{enc(fr'{_compile}')},{enc('__import__')}))),__{t}__:={args} if __{_str}__ else (getattr(KhangCoder({enc('ctypes')}),{enc('memset')})(0,0,1) if hasattr(KhangCoder({enc('ctypes')}),'memset') else {args}[::-0x01]),(No1 if __{_str}__ else getattr(({k} for {k} in ({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('khangcoder')}))),__{t}__)[-1]))()
    def {kwds}(Khangcoder, {arg_}):setattr(Khangcoder,{enc("Project6")},__{trunks}___);_Ox3[{enc('ToLaBuaYeu')}]={champ}({enc('1')});{HomNayToiBuon}[{enc(f'{_uni}')}]=lambda {c}:(lambda: getattr('',{enc('join')})(_{thicthamcrush}(__KhangCoder__({i})-{_anhxa1}) for {i} in {c}))();{m}=KhangCoder({enc('marshal')});__ToCrushCauMoa__=KhangCoder({enc("ctypes")});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_aychochoco}')},{champ}({enc('8+8')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('NgaoChoDaiDoanCuoi')},{champ}({enc('ord')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('XinChaoVietNam')},{champ}({enc('1+2')}));__{r}__=getattr(Khangcoder,{enc('__getattr__')})({arg_});__{r}__=getattr({m},{enc("loads")})(__{r}__);return getattr(KhangCoder({enc('builtins')}),{enc('BotㅤPyTiㅤAbi')})(__{r}__,globals(),globals())
    def __call__(Khangcoder, *{args}, **{kwds}):_Ox3[{enc(fr'_{a}')}]={champ}({enc('1')});{_globals}={HomNayToiBuon};{_globals}[{enc('___BoMayLaHeHe__')}]=lambda {c}:(lambda: getattr('',{enc('join')})(_{thicthamcrush}(__KhangCoder__({i})-{batconsocbovolo})for {i} in {c}))();(lambda _{thicthamcrush}_:(setattr(Khangcoder,{enc("Project7")},{siba}),___BoMayLaHeHe__({anhxa('0')}))[_{a}] if({_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(getattr(KhangCoder({enc('marshal')}),{enc('loads')})))=={enc("<class 'builtin_function_or_method'>")}) else getattr(({k} for {k} in(___BoMayLaHeHe__({anhxa('No1')}))),{enc('throw')})(___BoMayLaHeHe__({enc(fr'{args}')})))(___BoMayLaHeHe__({anhxa('0')}));getattr(Khangcoder,{enc(f'{kwds}')})((lambda {t}:({t} if isinstance({t},(getattr(KhangCoder({enc('builtins')}),{enc('bytes')}),getattr(KhangCoder({enc('builtins')}),{enc('bytearray')}))) else getattr(({k} for {k} in(___BoMayLaHeHe__({anhxa('No1')}))),{enc('throw')})({enc('Exception')}({enc('Khangcoder')}))))(__DuyObf__({args}[No1]).{s}()))

(lambda {kwds}:(getattr((lambda:No1).__globals__['__builtins__'],'__import__')('builtins'), __khangcoderㅤThaoMyCoder__()(),(lambda: getattr((lambda:No1).__globals__['__builtins__'], '__name__') and __PyTiㅤAbi__)(), {kwds}()))(__PyTiㅤAbiObfusCator__)

try:
    __PyTiㅤAbiObfusCator__()(bytecode)
except Exception:getattr(KhangCoder({enc('traceback')}),{enc('print_exc')})()
except KeyboardInterrupt:___BoMayLaHeHe__({anhxa('pass')})"""

def _gen_siba():
    return ''.join(random.choices([chr(i) for i in range(44032, 55204) if chr(i).isprintable() and chr(i).isidentifier()], k=11))
# alias for backward compat
siba_func = _gen_siba

def _moreobf(tree):
    import random, ast

    def junk(en, max_value):
        cases = []
        line = max_value + 1
        for i in range(random.randint(1, 5)):
            case_name = '__' + _gen_siba()
            case_body = [ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=en, ctx=ast.Load()), attr='args', ctx=ast.Load()), slice=ast.Constant(value=0), ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(value=line)]), body=[ast.Assign(targets=[ast.Name(id=case_name, ctx=ast.Store())], value=ast.Constant(value=random.randint(0xFFFFF, 0xFFFFFFFFFFFF)))], orelse=[])]
            cases.extend(case_body)
            line += 1
        return cases

    def bl(body):
        var = '__' + _gen_siba()
        en = '__' + _gen_siba()
        _memoryerror = f'{thicthamcrush}_'
        tb = [ast.AugAssign(target=ast.Name(id=var, ctx=ast.Store()), op=ast.Add(), value=ast.Constant(value=1)), ast.Try(body=[ast.Raise(exc=ast.Call(func=ast.Name(id=_memoryerror, ctx=ast.Load()), args=[ast.Name(id=var, ctx=ast.Load())], keywords=[]))], handlers=[ast.ExceptHandler(type=ast.Name(id=_memoryerror, ctx=ast.Load()), name=en, body=[])], orelse=[], finalbody=[])]
        for i, stmt in enumerate(body, start=1):
            tb[1].handlers[0].body.append(ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=en, ctx=ast.Load()), attr='args', ctx=ast.Load()), slice=ast.Constant(value=0), ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(value=i)]), body=[stmt], orelse=[]))
        tb[1].handlers[0].body.extend(junk(en, len(body)))
        node = ast.Assign(targets=[ast.Name(id=var, ctx=ast.Store())], value=ast.Constant(value=0))
        return [node] + tb

    def _bl(node):
        olb = node.body
        var = _gen_siba()
        en = _gen_siba()
        _memoryerror = f'{thicthamcrush}_'
        tb = [ast.AugAssign(target=ast.Name(id=var, ctx=ast.Store()), op=ast.Add(), value=ast.Constant(value=1)), ast.Try(body=[ast.Raise(exc=ast.Call(func=ast.Name(id=_memoryerror, ctx=ast.Load()), args=[ast.Name(id=var, ctx=ast.Load())], keywords=[]))], handlers=[ast.ExceptHandler(type=ast.Name(id=_memoryerror, ctx=ast.Load()), name=en, body=[])], orelse=[], finalbody=[])]
        for i, stmt in enumerate(olb, start=1):
            tb[1].handlers[0].body.append(ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=en, ctx=ast.Load()), attr='args', ctx=ast.Load()), slice=ast.Constant(value=0), ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(value=i)]), body=[stmt], orelse=[]))
        tb[1].handlers[0].body.extend(junk(en, len(olb)))
        node.body = [ast.Assign(targets=[ast.Name(id=var, ctx=ast.Store())], value=ast.Constant(value=0))] + tb
        return node

    def on(node):
        if isinstance(node, ast.FunctionDef):
            return _bl(node)
        return node
    nb = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            nb.append(on(node))
        elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign, ast.Expr)):
            nb.extend(bl([node]))
        elif isinstance(node, (ast.While, ast.For, ast.If)):
            node.body = sum([bl([x]) for x in node.body], [])
            nb.append(node)
        else:
            nb.append(node)
    tree.body = nb
    return tree

def __moreobf__(x):
    if isinstance(x, str):x = ast.parse(x)
    x = _moreobf(x)
    ast.fix_missing_locations(x)
    return x

def _syntax(x):
    def v(node):
        if getattr(node, 'name', None):
            for i, statement in enumerate(node.body):
                try:
                    c1 = ast.parse(f"{champ}('No1/No1')").body[0]
                    c2 = ast.parse(f'if "khangcoderbadao" == "suthanhcongobf":\n pass\nelse:\n pass').body[0]
                    ten = ast.Try(body=[c1, c2], handlers=[ast.ExceptHandler(type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()), name=None, body=[z(statement)])], orelse=[], finalbody=[])
                    node.body[i] = ten
                except Exception:
                    pass
            return node

    def z(statement):
        try:
            c1 = ast.parse(f"{champ}('No1/No1')").body[0]
            fb = ast.parse(f"{_str}(___BoMayLaHeHe__({anhxa('100')}))").body[0]
            return ast.Try(body=[c1], handlers=[ast.ExceptHandler(type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()), name=None, body=[statement])], orelse=[ast.Pass()], finalbody=[fb])
        except Exception:
            return statement
    try:
        tree = ast.parse(x)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                v(node)
        ast.fix_missing_locations(tree)
        return ast.unparse(tree)
    except Exception:
        return x

def _syntax1(x):
    def v(node):
        if getattr(node, 'name', None):
            nb=[]
            for st in node.body:
                try:
                    fi=ast.parse(f'if "{rd()}"!="{rd()}":\n {champ}(___BoMayLaHeHe__({anhxa("No1/No1")}))\nelse:\n pass').body[0]
                    fw=ast.parse(f"with _Ox5(___BoMayLaHeHe__({anhxa('__file__')}),{enc('r')}):\n pass").body[0]
                    ten=ast.Try(body=[fi,fw], handlers=[ast.ExceptHandler(type=ast.Name(id='ZeroDivisionError',ctx=ast.Load()),name=None,body=[z(st)])], orelse=[ast.Pass()], finalbody=[ast.parse(f'{_str}(___BoMayLaHeHe__({anhxa("100")}))').body[0]])
                    nb.append(ten)
                except Exception:
                    nb.append(st)
            node.body=nb
            return node

    def z(st):
        try:
            it=ast.Try(body=[ast.parse(f"{champ}('No1/No1')").body[0]], handlers=[ast.ExceptHandler(type=ast.Name(id='Exception',ctx=ast.Load()),name=None,body=[ast.Pass()])], orelse=[st], finalbody=[])
            return ast.Try(body=[it], handlers=[ast.ExceptHandler(type=ast.Name(id='ZeroDivisionError',ctx=ast.Load()),name=None,body=[st])], orelse=[ast.Pass()], finalbody=[ast.parse(f"{_str}(___BoMayLaHeHe__({anhxa('100')}))").body[0]])
        except Exception:
            return st

    try:
        t=ast.parse(x)
        for n in ast.walk(t):
            if isinstance(n,ast.FunctionDef):v(n)
        ast.fix_missing_locations(t)
        return ast.unparse(t)
    except Exception:
        return x

_str_ = f"{_str}"
def rd():
    return "�✦�✧�✧�_.._Anh6X✦�✧�..2g.@�Nguyen✧✦..�%.gay$.��Coder_�✦�" + "".join(__import__("random").sample([str(i) for i in range(44032, 55204)], k=3))
def random1():
    return '___Anh__Nguyen__Coder___' + "".join(__import__("random").sample([str(i) for i in range(1000, 3000)], k=3))
def random_match():
    var1 = ast.Constant(value=random1(), kind=None)
    var2 = ast.Constant(value=rd(), kind=None)
    return ast.Match(subject=ast.Compare(left=var1, ops=[ast.Eq()], comparators=[var2]), cases=[ast.match_case(pattern=ast.MatchValue(value=ast.Constant(value=True, kind=None)), body=[ast.Assign(lineno=0, col_offset=0, targets=[], value=[ast.Raise(exc=ast.Call(func=ast.Name(id=f'{thicthamcrush}_', ctx=ast.Load()), args=[], keywords=[ast.Constant(value=[True])]))])]), ast.match_case(pattern=ast.MatchValue(value=ast.Constant(value=False, kind=None)), body=[ast.Assign(lineno=0, col_offset=0, targets=[ast.Name(id=rd(), ctx=ast.Store())], value=ast.Constant(value=[[True], [False]], kind=None)), ast.Expr(lineno=0, col_offset=0, value=ast.Call(func=ast.Name(id=_str_, ctx=ast.Load()), args=[ast.Constant(value=[rd()], kind=None)], keywords=[]))])])
def trycatch(body, loop):
    ar = []
    for x in body:
        j = x
        for _ in range(1):
            j = ast.Try(body=[random_match()], handlers=[ast.ExceptHandler(type=ast.Name(id=f'{thicthamcrush}_', ctx=ast.Load()), name=rd(), body=[j])], orelse=[], finalbody=[])
            j.body.append(ast.Raise(exc=ast.Call(func=ast.Name(id=f'{thicthamcrush}_', ctx=ast.Load()), args=[], keywords=[ast.Constant(value=[True])]), cause=None))
        ar.append(j)
    return ar
def random_match1():
    var1 = ast.Constant(value=random1())
    var2 = ast.Constant(value=rd())
    cond = ast.Compare(left=var1, ops=[ast.Eq()], comparators=[var2])
    return ast.If(test=cond, body=[ast.Raise(exc=ast.Call(func=ast.Name(id=f'{thicthamcrush}_', ctx=ast.Load()), args=[], keywords=[]), cause=None)], orelse=[ast.Assign(targets=[ast.Name(id=rd(), ctx=ast.Store())], value=ast.Constant(value=[[True], [False]])), ast.Expr(value=ast.Call(func=ast.Name(id=_str_, ctx=ast.Load()), args=[ast.Constant(value=rd())], keywords=[]))])

def trycatch1(body, loop):
    ar = []
    for x in body:
        j = x
        for _ in range(1):
            j = ast.Try(body=[random_match1()], handlers=[ast.ExceptHandler(type=ast.Name(id=f'{thicthamcrush}_', ctx=ast.Load()), name=rd(), body=[j])], orelse=[], finalbody=[])
            j.body.append(ast.Raise(exc=ast.Call(func=ast.Name(id=f'{thicthamcrush}_', ctx=ast.Load()), args=[], keywords=[]), cause=None))
        ar.append(j)
    return ar

def joinstr(f):
    if not isinstance(f, ast.JoinedStr):
        return f
    vl = []
    for i in f.values:
        if isinstance(i, ast.Constant):
            vl.append(i)
        elif isinstance(i, ast.FormattedValue):
            value_expr = i.value
            if i.conversion == 115:
                value_expr = Call(func=Name(id=f'{_str}', ctx=Load()), args=[value_expr], keywords=[])
            elif i.conversion == 114:
                value_expr = Call(func=Name(id='repr', ctx=Load()), args=[value_expr], keywords=[])
            elif i.conversion == 97:
                value_expr = Call(func=Name(id='ascii', ctx=Load()), args=[value_expr], keywords=[])
            if i.format_spec:
                if isinstance(i.format_spec, ast.JoinedStr):
                    spec_expr = joinstr(i.format_spec)
                elif isinstance(i.format_spec, ast.Constant):
                    spec_expr = i.format_spec
                elif isinstance(i.format_spec, ast.FormattedValue):
                    spec_parts = []
                    spec_value = i.format_spec.value
                    if i.format_spec.conversion == 115:
                        spec_value = Call(func=Name(id=f'{_str}', ctx=Load()), args=[spec_value], keywords=[])
                    elif i.format_spec.conversion == 114:
                        spec_value = Call(func=Name(id='repr', ctx=Load()), args=[spec_value], keywords=[])
                    elif i.format_spec.conversion == 97:
                        spec_value = Call(func=Name(id='ascii', ctx=Load()), args=[spec_value], keywords=[])
                    spec_expr = spec_value
                else:
                    spec_expr = i.format_spec
                value_expr = Call(func=Name(id='format', ctx=Load()), args=[value_expr, spec_expr], keywords=[])
            elif i.conversion == -1:
                value_expr = Call(func=Name(id=f'{_str}', ctx=Load()), args=[value_expr], keywords=[])
            vl.append(value_expr)
        elif hasattr(i, 'values') and isinstance(i, ast.JoinedStr):
            vl.append(joinstr(i))
        else:
            vl.append(Call(func=Name(id=f'{_str}', ctx=Load()), args=[i], keywords=[]))
    if not vl:
        return Constant(value='')
    if len(vl) == 1 and isinstance(vl[0], ast.Constant):
        return vl[0]
    return Call(func=Attribute(value=Constant(value=''), attr='join', ctx=Load()), args=[Tuple(elts=vl, ctx=Load())], keywords=[])

class cv(ast.NodeTransformer):

    def visit_JoinedStr(self, node):
        node = joinstr(node)
        return node

buitlins = ['ascii', 'input', 'ord', 'len', 'getattr', 'globals', 'open', 'vars', 'object', 'float', 'print','exec', 'eval', 'compile', '__import__','map', 'filter', 'format','enumerate', 'iter', 'next', 'pow', 'isinstance', 'any', 'hasattr','repr', 'sum', 'min', 'max', 'hex']

class hide(ast.NodeTransformer):

    def visit_Name(self, node):
        if node.id in buitlins:
            node = Call(func=Name(id='getattr', ctx=Load()), args=[Call(func=Name(id='KhangCoder', ctx=Load()), args=[Constant(value='builtins')], keywords=[]), Constant(value=node.id)], keywords=[])
        return node

class hide1(ast.NodeTransformer):

    def visit_Name(self, node):
        if node.id in buitlins:
            return Subscript(value=Call(func=Name(id=f'{_vars}', ctx=Load()), args=[Subscript(value=Call(func=Call(func=Name(id='getattr', ctx=Load()), args=[Call(func=Name(id='KhangCoder', ctx=Load()), args=[Constant(value='builtins')], keywords=[]), Name(id="DoMayBietNoLaGi", ctx=Load())], keywords=[]), args=[], keywords=[]), slice=Name(id=f"{enc('__builtins__')}", ctx=Load()))], keywords=[]), slice=Constant(value=node.id), ctx=Load())
        return node

class obf1(ast.NodeTransformer):

    _SAFE_INT_MAX = 500000
    @staticmethod
    def _float_safe_for_v1(f):
        try:
            nguyen = int(f)
            thapphan = int(str(f).split('.')[-1])
            dodai = len(str(thapphan))
            return max(abs(nguyen), abs(thapphan), abs(dodai)) <= obf1._SAFE_INT_MAX
        except Exception:
            return False

    def visit_Constant(self, node):
        if isinstance(node.value, bool):
            return node
        if isinstance(node.value, str):
            node = obfstr1(node.value)
        elif isinstance(node.value, int):
            if abs(node.value) <= self._SAFE_INT_MAX:
                node = obfint1(node.value)
            else:
                node = obfint2(node.value)
        elif isinstance(node.value, float):
            if self._float_safe_for_v1(node.value):
                node = obffloat1(node.value)
            else:
                node = obffloat2(node.value)
        return node

class obf2(ast.NodeTransformer):

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            node = obfstr2(node.value)
        elif isinstance(node.value, int):
            node = obfint2(node.value)
        elif isinstance(node.value, float):
            node = obffloat2(node.value)
        return node

class obf3(ast.NodeTransformer):

    _SAFE_INT_MAX = 500000
    @staticmethod
    def _float_safe_for_v3(f):
        try:
            nguyen = int(f)
            thapphan = int(str(f).split('.')[-1])
            dodai = len(str(thapphan))
            return max(abs(nguyen), abs(thapphan), abs(dodai)) <= obf3._SAFE_INT_MAX
        except Exception:
            return False

    def visit_Constant(self, node):
        if isinstance(node.value, bool):
            return node
        if isinstance(node.value, str):
            node = obfstr3(node.value)
        elif isinstance(node.value, int):
            if abs(node.value) <= self._SAFE_INT_MAX:
                node = obfint3(node.value)
            else:
                node = obfint2(node.value)
        elif isinstance(node.value, float):
            if self._float_safe_for_v3(node.value):
                node = obffloat3(node.value)
            else:
                node = obffloat2(node.value)
        return node

# =====================================================================================================
# PYTI DEDICATED STRING MACHINE (STRING V4 ENGINE)
# =====================================================================================================

_PYTI_STR_MACHINE_ID = f"__PyTi_StrMachine_{uuid.uuid4().hex[:8]}__"
_PYTI_STR_MACHINE_V5_ID = f"__PyTi_StrM5_{uuid.uuid4().hex[:8]}__"

class PyTiStringMachineCompiler:
    OP_NOP = 0
    OP_IMM = 1
    OP_LOAD_R = 2
    OP_STORE_R = 3
    OP_ADD = 4
    OP_SUB = 5
    OP_XOR = 6
    OP_ROL = 7
    OP_ROR = 8
    OP_INV = 9
    OP_EMIT = 10
    OP_EMIT_STREAM = 11
    OP_JUMP = 12
    OP_JUMP_IF_Z = 13
    OP_JUMP_IF_NZ = 14
    OP_HALT = 15
    NUM_OPS = 16

    def __init__(self):
        pass

    def compile(self, s: str) -> bytes:
        if not isinstance(s, str):
            s = str(s)
        raw_bytes = s.encode('utf-8', errors='surrogatepass')
        seed = random.randint(0x10000000, 0x7FFFFFFF)
        
        ins = []
        extra_data = bytearray()
        
        if len(raw_bytes) == 0:
            ins.append((self.OP_HALT, 0))
        elif len(raw_bytes) <= 24:
            for b in raw_bytes:
                self._compile_byte(b, ins)
            ins.append((self.OP_HALT, 0))
        else:
            head_len = min(4, len(raw_bytes))
            tail_len = min(4, max(0, len(raw_bytes) - head_len))
            mid_len = len(raw_bytes) - head_len - tail_len
            
            for i in range(head_len):
                self._compile_byte(raw_bytes[i], ins)
                
            if mid_len > 0:
                pos = head_len
                end_pos = len(raw_bytes) - tail_len
                while pos < end_pos:
                    chunk_sz = min(random.randint(64, 256), end_pos - pos)
                    chunk = raw_bytes[pos:pos + chunk_sz]
                    stream_offset = len(extra_data)
                    # FIX BUG #4: per-build stream key (no static 0x1F1F1F1F/0x5A5A5A5A fingerprint)
                    s_key = (seed ^ (stream_offset * _PYTI_SM_K1_MUL + _PYTI_SM_K1_ADD)) & 0x7FFFFFFF
                    for mb in chunk:
                        s_key = (s_key * 1103515245 + 12345) & 0x7FFFFFFF
                        extra_data.append(mb ^ (s_key & 0xFF))
                    ins.append((self.OP_EMIT_STREAM, chunk_sz))
                    pos += chunk_sz
                    if pos < end_pos and random.random() < 0.25:
                        self._compile_byte(raw_bytes[pos], ins)
                        pos += 1
                
            for i in range(len(raw_bytes) - tail_len, len(raw_bytes)):
                self._compile_byte(raw_bytes[i], ins)
                
            ins.append((self.OP_HALT, 0))

        final_ins = []
        for op, arg in ins:
            if op != self.OP_HALT and random.random() < 0.12:
                junk = random.choice([
                    (self.OP_NOP, random.randint(0, 0xFFFF)),
                    (self.OP_STORE_R, random.randint(0, 3)),
                ])
                final_ins.append(junk)
            final_ins.append((op, arg))

        ins_bytes = bytearray()
        for i, (op, arg) in enumerate(final_ins):
            # FIX BUG #4: per-build rolling keys (no static 0x9E3779B9/0xC2B2AE35)
            k1 = ((seed ^ ((i + 1) * _PYTI_SM_K1_MUL) + _PYTI_SM_K1_ADD) & 0xFFFFFFFF)
            k2 = ((seed ^ ((i + 1) * _PYTI_SM_K2_MUL) + _PYTI_SM_K2_ADD) & 0xFFFFFFFF)
            raw_op = (op ^ (k1 & 0xFF)) & 0xFF
            raw_arg = (arg ^ k2) & 0xFFFFFFFF
            ins_bytes.extend(struct.pack('>BI', raw_op, raw_arg))

        body = bytes(ins_bytes) + bytes(extra_data)
        chk = zlib.adler32(body) & 0xFFFFFFFF
        total_count = len(final_ins)

        comp_body = zlib.compress(body, 9)
        # FIX BUG #4: per-build magic (no static 0x5054)
        hdr = struct.pack('>HI3I', _PYTI_SM_MAGIC, chk, seed, total_count, len(body))
        return hdr + comp_body

    def _compile_byte(self, b: int, ins: list):
        mode = random.randint(1, 7)
        if mode == 1:
            k = random.randint(1, 255)
            imm = b ^ k
            ins.append((self.OP_IMM, imm))
            ins.append((self.OP_XOR, k))
            ins.append((self.OP_EMIT, 0))
        elif mode == 2:
            k = random.randint(1, 255)
            imm = (b - k) & 0xFF
            ins.append((self.OP_IMM, imm))
            ins.append((self.OP_ADD, k))
            ins.append((self.OP_EMIT, 0))
        elif mode == 3:
            k = random.randint(1, 255)
            imm = (b + k) & 0xFF
            ins.append((self.OP_IMM, imm))
            ins.append((self.OP_SUB, k))
            ins.append((self.OP_EMIT, 0))
        elif mode == 4:
            shift = random.randint(1, 7)
            k = random.randint(1, 255)
            target = b ^ k
            imm = (((target >> shift) | (target << (8 - shift))) & 0xFF)
            ins.append((self.OP_IMM, imm))
            ins.append((self.OP_ROL, shift))
            ins.append((self.OP_XOR, k))
            ins.append((self.OP_EMIT, 0))
        elif mode == 5:
            imm = (~b) & 0xFF
            ins.append((self.OP_IMM, imm))
            ins.append((self.OP_INV, 0))
            ins.append((self.OP_EMIT, 0))
        elif mode == 6:
            shift = random.randint(1, 7)
            k = random.randint(1, 255)
            target = (b - k) & 0xFF
            imm = (((target << shift) | (target >> (8 - shift))) & 0xFF)
            ins.append((self.OP_IMM, imm))
            ins.append((self.OP_ROR, shift))
            ins.append((self.OP_ADD, k))
            ins.append((self.OP_EMIT, 0))
        elif mode == 7:
            r = random.randint(0, 3)
            k = random.randint(1, 255)
            imm = b ^ k
            ins.append((self.OP_IMM, imm))
            ins.append((self.OP_STORE_R, r))
            ins.append((self.OP_LOAD_R, r))
            ins.append((self.OP_XOR, k))
            ins.append((self.OP_EMIT, 0))

def generate_string_machine_runtime(machine_name: str) -> str:
    # FIX BUG #4: embed per-build magic/keys so every build has different fingerprint.
    _sm_magic = _PYTI_SM_MAGIC
    _sm_k1m = _PYTI_SM_K1_MUL
    _sm_k1a = _PYTI_SM_K1_ADD
    _sm_k2m = _PYTI_SM_K2_MUL
    _sm_k2a = _PYTI_SM_K2_ADD
    inner_code = f'''def {machine_name}(__pkg__, __memo__={{}}):
    try:
        import sys as __sys__
        if __sys__.gettrace() is not None:
            __sys__.settrace(None)
            return ""
        try:
            import threading as __th__
            if getattr(__th__, '_trace_hook', None) is not None:
                __th__.settrace(None)
                return ""
        except:
            pass
        try:
            __cf__ = __sys__._getframe()
            if __cf__.f_trace is not None:
                __cf__.f_trace = None
                __sys__.settrace(None)
                return ""
            if __cf__.f_back and __cf__.f_back.f_trace is not None:
                __cf__.f_back.f_trace = None
                __sys__.settrace(None)
                return ""
        except:
            pass

        if (0 if (1 if 0 else 2) else 3) != 3:
            _w_bomb = (_w0 := (_w1 := 0))
        if (1337 ^ 1337) != 0:
            _g_bomb = (lambda: (yield from (lambda: (yield 1))()))

        if __pkg__ in __memo__:
            return __memo__[__pkg__]
        import struct as __st__, zlib as __zl__
        if not isinstance(__pkg__, (bytes, bytearray)):
            try:
                import base64 as __b64__
                __pkg__ = __b64__.b85decode(__pkg__)
            except:
                return str(__pkg__)
        if len(__pkg__) < 18:
            return ""
        __magic__, __chk__, __seed__, __total_ins__, __body_len__ = __st__.unpack_from('>HI3I', __pkg__, 0)
        if __magic__ != {_sm_magic}:
            return ""
        __comp_body__ = __pkg__[18:]
        try:
            __body__ = __zl__.decompress(__comp_body__)
        except:
            __body__ = __comp_body__
        if (__zl__.adler32(__body__) & 0xFFFFFFFF) != __chk__ or len(__body__) != __body_len__:
            return ""
        
        __ins_bytes__ = __body__[:__total_ins__ * 5]
        __extra__ = __body__[__total_ins__ * 5:]
        __extra_ptr__ = 0
        
        __acc__ = 0
        __r__ = [0, 0, 0, 0]
        __tape__ = bytearray()
        __pc__ = 0
        __steps__ = 0
        __max_steps__ = __total_ins__ * 8 + 256
        
        while __pc__ < __total_ins__ and __steps__ < __max_steps__:
            __steps__ += 1
            if (__steps__ & 0x1F) == 0:
                if __sys__.gettrace() is not None:
                    __sys__.settrace(None)
                    return ""
            __raw_op__, __raw_arg__ = __st__.unpack_from('>BI', __ins_bytes__, __pc__ * 5)
            __k1__ = ((__seed__ ^ ((__pc__ + 1) * {_sm_k1m}) + {_sm_k1a}) & 0xFFFFFFFF)
            __k2__ = ((__seed__ ^ ((__pc__ + 1) * {_sm_k2m}) + {_sm_k2a}) & 0xFFFFFFFF)
            __op__ = (__raw_op__ ^ (__k1__ & 0xFF)) & 0xFF
            __arg__ = (__raw_arg__ ^ __k2__) & 0xFFFFFFFF
            __pc__ += 1
            
            if __op__ == 0:
                continue
            elif __op__ == 1:
                __acc__ = __arg__ & 0xFF
            elif __op__ == 2:
                __acc__ = __r__[__arg__ % 4] & 0xFF
            elif __op__ == 3:
                __r__[__arg__ % 4] = __acc__ & 0xFF
            elif __op__ == 4:
                __acc__ = (__acc__ + (__arg__ & 0xFF)) & 0xFF
            elif __op__ == 5:
                __acc__ = (__acc__ - (__arg__ & 0xFF)) & 0xFF
            elif __op__ == 6:
                __acc__ = (__acc__ ^ (__arg__ & 0xFF)) & 0xFF
            elif __op__ == 7:
                __s__ = __arg__ & 7
                __acc__ = (((__acc__ << __s__) | (__acc__ >> (8 - __s__))) & 0xFF) if __s__ else __acc__
            elif __op__ == 8:
                __s__ = __arg__ & 7
                __acc__ = (((__acc__ >> __s__) | (__acc__ << (8 - __s__))) & 0xFF) if __s__ else __acc__
            elif __op__ == 9:
                __acc__ = (~__acc__) & 0xFF
            elif __op__ == 10:
                __tape__.append(__acc__ & 0xFF)
            elif __op__ == 11:
                __cnt__ = __arg__
                __chunk__ = __extra__[__extra_ptr__:__extra_ptr__ + __cnt__]
                __s_key__ = (__seed__ ^ (__extra_ptr__ * {_sm_k1m} + {_sm_k1a})) & 0x7FFFFFFF
                for __b__ in __chunk__:
                    __s_key__ = (__s_key__ * 1103515245 + 12345) & 0x7FFFFFFF
                    __tape__.append(__b__ ^ (__s_key__ & 0xFF))
                __extra_ptr__ += __cnt__
            elif __op__ == 12:
                __pc__ = __arg__ % __total_ins__
            elif __op__ == 13:
                if (__acc__ & 0xFF) == 0:
                    __pc__ = __arg__ % __total_ins__
            elif __op__ == 14:
                if (__acc__ & 0xFF) != 0:
                    __pc__ = __arg__ % __total_ins__
            elif __op__ == 15:
                break
                
        __res__ = __tape__.decode('utf-8', errors='surrogatepass')
        if len(__memo__) < 10000:
            __memo__[__pkg__] = __res__
        try:
            __sys__._getframe().f_trace = None
        except:
            pass
        return __res__
    except:
        return ""
try:
    getattr(__import__('builtins'), '__dict__')[{machine_name!r}] = {machine_name}
    setattr(__import__('builtins'), {machine_name!r}, {machine_name})
except:
    pass
'''
    # FIX BUG #4: fragmented loader + indirect imports (no 1-line exec(b85...) pattern).
    _raw_inner = zlib.compress(inner_code.encode('utf-8'), 9)
    _frag = _pyti_b85_frag_expr(_raw_inner)
    _v1 = '_z' + uuid.uuid4().hex[:5]
    _v2 = '_b' + uuid.uuid4().hex[:5]
    _imp_z = _pyti_chr_expr('zlib')
    _imp_b = _pyti_chr_expr('base64')
    return (
        f"{_v1}=__import__({_imp_z});{_v2}=__import__({_imp_b});"
        f"exec({_v1}.decompress({_v2}.b85decode({_frag})).decode('utf-8'))"
    )

def inject_string_machine(tree: ast.Module, machine_name: str = None) -> ast.Module:
    if machine_name is None:
        machine_name = _PYTI_STR_MACHINE_ID
    if getattr(tree, f'_pyti_sm_{machine_name}', False):
        return tree
    for stmt in getattr(tree, 'body', []):
        if isinstance(stmt, ast.FunctionDef) and stmt.name == machine_name:
            return tree
    setattr(tree, f'_pyti_sm_{machine_name}', True)
    runtime_src = generate_string_machine_runtime(machine_name)
    try:
        dec_tree = ast.parse(runtime_src)
        fut_idx = 0
        while fut_idx < len(tree.body) and isinstance(tree.body[fut_idx], ast.ImportFrom) and tree.body[fut_idx].module == '__future__':
            fut_idx += 1
        tree.body = tree.body[:fut_idx] + dec_tree.body + tree.body[fut_idx:]
        ast.fix_missing_locations(tree)
    except Exception:
        pass
    return tree

def obfstr4(s: str, machine_name: str = None):
    if machine_name is None:
        machine_name = _PYTI_STR_MACHINE_ID
    compiler = PyTiStringMachineCompiler()
    pkg = compiler.compile(s)
    return ast.Call(
        func=ast.Name(id=machine_name, ctx=ast.Load()),
        args=[ast.Constant(value=pkg)],
        keywords=[]
    )

class obf4(ast.NodeTransformer):
    _SAFE_INT_MAX = 500000

    def __init__(self, machine_name: str = None, inject_into_module: bool = False):
        self.machine_name = machine_name or _PYTI_STR_MACHINE_ID
        self.inject_into_module = inject_into_module
        self.compiler = PyTiStringMachineCompiler()
        self.injected = False
        super().__init__()

    def visit_JoinedStr(self, node):
        return node

    def visit_MatchValue(self, node):
        return node

    def visit_Module(self, node):
        self.generic_visit(node)
        if self.inject_into_module and not self.injected:
            inject_string_machine(node, self.machine_name)
            self.injected = True
        return node

    def visit_Constant(self, node):
        if isinstance(node.value, bool):
            return node
        if isinstance(node.value, str):
            node = obfstr4(node.value, self.machine_name)
        elif isinstance(node.value, int):
            node = obfint2(node.value)
        elif isinstance(node.value, float):
            node = obffloat2(node.value)
        return node

# =====================================================================================================
# PYTI STRING MACHINE V5 (STRONGER THAN V4, SLIGHTLY BIGGER)
# V4 weaknesses fixed: LCG stream -> SHA256-CTR, plaintext seed -> pepper-masked seed,
# single bytes blob -> fragmented blob, single call shape -> 4 poly shapes,
# plain dict memo -> hashed capped cache + anti-trace, dead JUMP ops -> real CMOV/MUL/ROL modes.
# Python 3.9 compatible. No emojis in generated code.
# =====================================================================================================

def _pyti_v5_modinv_odd(a: int) -> int:
    a &= 0xFF
    # inverse of odd a modulo 256 (exists for all odd a)
    inv = 1
    for _ in range(6):
        inv = (inv * (2 - a * inv)) & 0xFF
    return inv


def _pyti_v5_ror8(v: int, s: int) -> int:
    s &= 7
    if s == 0:
        return v & 0xFF
    return (((v >> s) | (v << (8 - s))) & 0xFF)


def _pyti_v5_rol8(v: int, s: int) -> int:
    s &= 7
    if s == 0:
        return v & 0xFF
    return (((v << s) | (v >> (8 - s))) & 0xFF)


def _pyti_v5_keystream(key: bytes, n: int) -> bytes:
    # SHA256-CTR expansion (much stronger than V4 LCG)
    try:
        import hashlib as _hl5
    except Exception:
        return bytes(((key[i % len(key)] + i) & 0xFF) for i in range(n)) if key else bytes(n)
    out = bytearray()
    ctr = 0
    while len(out) < n:
        try:
            out.extend(_hl5.sha256(key + ctr.to_bytes(4, 'big')).digest())
        except Exception:
            break
        ctr += 1
    return bytes(out[:n])


def _pyti_v5_pepper32() -> int:
    try:
        return int(str(_PYTI_BUILD_PEPPER)[:8], 16) & 0xFFFFFFFF
    except Exception:
        return 0x5A5A5A5A


class PyTiStringMachineV5Compiler:
    # V4 ops 0..15 kept with identical semantics, new ops 16..23 added.
    OP_NOP = 0
    OP_IMM = 1
    OP_LOAD_R = 2
    OP_STORE_R = 3
    OP_ADD = 4
    OP_SUB = 5
    OP_XOR = 6
    OP_ROL = 7
    OP_ROR = 8
    OP_INV = 9
    OP_EMIT = 10
    OP_EMIT_STREAM = 11
    OP_JUMP = 12
    OP_JUMP_IF_Z = 13
    OP_JUMP_IF_NZ = 14
    OP_HALT = 15
    OP_MUL = 16
    OP_ADDROL = 17
    OP_XORROL = 18
    OP_SWAP_R = 19
    OP_PUSH = 20
    OP_POP = 21
    OP_CMOV_Z = 22
    OP_MIX = 23
    NUM_OPS = 24

    def __init__(self):
        pass

    def compile(self, s: str) -> bytes:
        if not isinstance(s, str):
            s = str(s)
        raw_bytes = s.encode('utf-8', errors='surrogatepass')
        seed = random.randint(0x10000000, 0x7FFFFFFF)
        try:
            salt = secrets.token_bytes(4)
        except Exception:
            salt = bytes(random.randint(0, 255) for _ in range(4))
        ins = []
        extra_data = bytearray(salt)  # first 4 bytes of extra are the salt
        if len(raw_bytes) == 0:
            ins.append((self.OP_HALT, 0))
        elif len(raw_bytes) <= 16:
            # compact mode: 2-3 ins per byte (smaller than V4 for tiny strings)
            for b in raw_bytes:
                self._compile_byte_compact(b, ins)
            ins.append((self.OP_HALT, 0))
        else:
            head_len = min(3, len(raw_bytes))
            tail_len = min(3, max(0, len(raw_bytes) - head_len))
            for i in range(head_len):
                self._compile_byte_v5(raw_bytes[i], ins)
            pos = head_len
            end_pos = len(raw_bytes) - tail_len
            # single continuous CTR stream over middle bytes (offset = bytes already emitted)
            _mid_len = max(0, end_pos - pos)
            try:
                _base = self._stream_base(seed, salt)
                _ks_full = _pyti_v5_keystream(_base, _mid_len)
            except Exception:
                _ks_full = bytes(_mid_len)
            _ks_pos = 0
            while pos < end_pos:
                chunk_sz = min(random.randint(48, 192), end_pos - pos)
                chunk = raw_bytes[pos:pos + chunk_sz]
                ks = _ks_full[_ks_pos:_ks_pos + chunk_sz]
                for j, mb in enumerate(chunk):
                    extra_data.append(mb ^ ks[j])
                _ks_pos += chunk_sz
                ins.append((self.OP_EMIT_STREAM, chunk_sz))
                pos += chunk_sz
                if pos < end_pos and random.random() < 0.15:
                    self._compile_byte_v5(raw_bytes[pos], ins)
                    pos += 1
            for i in range(len(raw_bytes) - tail_len, len(raw_bytes)):
                self._compile_byte_v5(raw_bytes[i], ins)
            ins.append((self.OP_HALT, 0))
        # integrity: 2 bytes of sha256(raw) packed into HALT arg
        try:
            import hashlib as _hl5i
            _dg = _hl5i.sha256(raw_bytes).digest()
            _chk2 = (_dg[0] << 8) | _dg[1]
        except Exception:
            _chk2 = (zlib.adler32(raw_bytes) & 0xFFFF) if raw_bytes else 0
        if ins and ins[-1][0] == self.OP_HALT:
            ins[-1] = (self.OP_HALT, _chk2 & 0xFFFF)
        # junk: only acc/stack-neutral ops (NOP or balanced PUSH+POP).
        # NOTE: never use register-writing junk here: modes 9/10 use STORE/LOAD
        # sequences and any register write in between would corrupt decoding.
        final_ins = []
        for op, arg in ins:
            if op != self.OP_HALT and random.random() < 0.10:
                if random.random() < 0.5:
                    final_ins.append((self.OP_NOP, random.randint(0, 0xFFFF)))
                else:
                    final_ins.append((self.OP_PUSH, 0))
                    final_ins.append((self.OP_POP, 0))
            final_ins.append((op, arg))
        # pack with rolling keys (24-op space)
        ins_bytes = bytearray()
        for i, (op, arg) in enumerate(final_ins):
            k1 = ((seed ^ ((i + 1) * _PYTI_SM_K1_MUL) + _PYTI_SM_K1_ADD) & 0xFFFFFFFF)
            k2 = ((seed ^ ((i + 1) * _PYTI_SM_K2_MUL) + _PYTI_SM_K2_ADD) & 0xFFFFFFFF)
            raw_op = (op + ((k1 & 0xFF) % self.NUM_OPS)) % self.NUM_OPS
            raw_arg = (arg ^ k2) & 0xFFFFFFFF
            ins_bytes.extend(struct.pack('>BI', raw_op, raw_arg))
        body = bytes(ins_bytes) + bytes(extra_data)
        chk = zlib.adler32(body) & 0xFFFFFFFF
        total_count = len(final_ins)
        comp_body = zlib.compress(body, 9)
        magic_v5 = (_PYTI_SM_MAGIC ^ 0x5A5A) & 0xFFFF
        seed_enc = (seed ^ _pyti_v5_pepper32()) & 0xFFFFFFFF
        hdr = struct.pack('>HI3I', magic_v5, chk, seed_enc, total_count, len(body))
        return hdr + comp_body

    def _stream_base(self, seed: int, salt: bytes) -> bytes:
        try:
            import hashlib as _hl5k
            return _hl5k.sha256(
                str(_PYTI_BUILD_PEPPER).encode() + seed.to_bytes(4, 'big') + bytes(salt)
            ).digest()
        except Exception:
            base = (seed.to_bytes(4, 'big') + bytes(salt))[:16]
            if len(base) < 16:
                base = (base * 4)[:16]
            return base

    def _compile_byte_compact(self, b: int, ins: list):
        # 2 modes only: XOR or ADD (smallest encoding)
        if random.random() < 0.5:
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, b ^ k))
            ins.append((self.OP_XOR, k))
        else:
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, (b - k) & 0xFF))
            ins.append((self.OP_ADD, k))
        ins.append((self.OP_EMIT, 0))

    def _compile_byte_v5(self, b: int, ins: list):
        mode = random.randint(1, 10)
        if mode <= 4:
            # reuse V4-style modes 1..4 (XOR/ADD/SUB/ROL+XOR)
            if mode == 1:
                k = random.randint(1, 255)
                ins.append((self.OP_IMM, b ^ k))
                ins.append((self.OP_XOR, k))
                ins.append((self.OP_EMIT, 0))
            elif mode == 2:
                k = random.randint(1, 255)
                ins.append((self.OP_IMM, (b - k) & 0xFF))
                ins.append((self.OP_ADD, k))
                ins.append((self.OP_EMIT, 0))
            elif mode == 3:
                k = random.randint(1, 255)
                ins.append((self.OP_IMM, (b + k) & 0xFF))
                ins.append((self.OP_SUB, k))
                ins.append((self.OP_EMIT, 0))
            else:
                shift = random.randint(1, 7)
                k = random.randint(1, 255)
                target = b ^ k
                ins.append((self.OP_IMM, _pyti_v5_ror8(target, shift)))
                ins.append((self.OP_ROL, shift))
                ins.append((self.OP_XOR, k))
                ins.append((self.OP_EMIT, 0))
        elif mode == 5:
            ins.append((self.OP_IMM, (~b) & 0xFF))
            ins.append((self.OP_INV, 0))
            ins.append((self.OP_EMIT, 0))
        elif mode == 6:
            # NEW: MUL with odd k (invertible mod 256)
            k = random.choice([1, 3, 5, 7, 9, 11, 13, 17, 19, 25, 27, 31, 37, 51, 53, 91, 127, 137, 151, 157, 171, 181, 191, 193, 199, 203, 213, 239, 241, 247, 255])
            inv = _pyti_v5_modinv_odd(k)
            ins.append((self.OP_IMM, (b * inv) & 0xFF))
            ins.append((self.OP_MUL, k))
            ins.append((self.OP_EMIT, 0))
        elif mode == 7:
            # NEW: ADDROL packed arg
            k_add = random.randint(1, 255)
            shift = random.randint(1, 7)
            target = _pyti_v5_ror8(b, shift)
            ins.append((self.OP_IMM, (target - k_add) & 0xFF))
            ins.append((self.OP_ADDROL, ((k_add << 3) | shift) & 0xFFFFFFFF))
            ins.append((self.OP_EMIT, 0))
        elif mode == 8:
            # NEW: XORROL packed arg
            k_xor = random.randint(1, 255)
            shift = random.randint(1, 7)
            target = _pyti_v5_ror8(b, shift)
            ins.append((self.OP_IMM, target ^ k_xor))
            ins.append((self.OP_XORROL, ((k_xor << 3) | shift) & 0xFFFFFFFF))
            ins.append((self.OP_EMIT, 0))
        elif mode == 9:
            # register dance ending with real decode (identity swaps around it)
            r = random.randint(0, 3)
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, b ^ k))
            ins.append((self.OP_STORE_R, r))
            ins.append((self.OP_SWAP_R, r))
            ins.append((self.OP_SWAP_R, r))
            ins.append((self.OP_LOAD_R, r))
            ins.append((self.OP_XOR, k))
            ins.append((self.OP_EMIT, 0))
        else:
            # PUSH/POP identity pair + CMOV identity + simple XOR
            r = random.randint(0, 3)
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, b ^ k))
            ins.append((self.OP_PUSH, 0))
            ins.append((self.OP_POP, 0))
            ins.append((self.OP_STORE_R, r))
            ins.append((self.OP_CMOV_Z, r))
            ins.append((self.OP_XOR, k))
            ins.append((self.OP_EMIT, 0))


def generate_string_machine_v5_runtime(machine_name: str) -> str:
    _sm_magic_v5 = (_PYTI_SM_MAGIC ^ 0x5A5A) & 0xFFFF
    _sm_k1m = _PYTI_SM_K1_MUL
    _sm_k1a = _PYTI_SM_K1_ADD
    _sm_k2m = _PYTI_SM_K2_MUL
    _sm_k2a = _PYTI_SM_K2_ADD
    _pep32 = _pyti_v5_pepper32()
    _bpep = str(_PYTI_BUILD_PEPPER)
    inner_code = f'''def {machine_name}(__pkg__, __c__=None):
    try:
        import sys as __sys__
        if __sys__.gettrace() is not None:
            __sys__.settrace(None)
            return ""
        try:
            __cf__ = __sys__._getframe()
            if __cf__.f_trace is not None:
                __cf__.f_trace = None
                __sys__.settrace(None)
                return ""
            if __cf__.f_back is not None and __cf__.f_back.f_trace is not None:
                __cf__.f_back.f_trace = None
                __sys__.settrace(None)
                return ""
        except:
            pass
        if (0 if (1 if 0 else 2) else 3) != 3:
            _w_bomb = (_w0 := (_w1 := 0))
        if (1337 ^ 1337) != 0:
            _g_bomb = (lambda: (yield from (lambda: (yield 1))()))
        try:
            import hashlib as __hl__
            __key__ = str(__pkg__.__class__.__name__)
        except:
            __key__ = "x"
        try:
            __ck__ = __hl__.sha256(bytes(__pkg__)).hexdigest() if isinstance(__pkg__, (bytes, bytearray)) else __hl__.sha256(str(__pkg__).encode()).hexdigest()
        except:
            __ck__ = str(len(str(__pkg__)))
        try:
            __cache__ = getattr({machine_name}, "_c", None)
            if not isinstance(__cache__, dict):
                __cache__ = {{}}
                setattr({machine_name}, "_c", __cache__)
            if __ck__ in __cache__:
                return __cache__[__ck__]
        except:
            __cache__ = None
        import struct as __st__, zlib as __zl__
        if not isinstance(__pkg__, (bytes, bytearray)):
            try:
                import base64 as __b64__
                __pkg__ = __b64__.b85decode(__pkg__)
            except:
                return str(__pkg__)
        if len(__pkg__) < 18:
            return ""
        __magic__, __chk__, __seed_enc__, __total_ins__, __body_len__ = __st__.unpack_from('>HI3I', __pkg__, 0)
        if __magic__ != {_sm_magic_v5}:
            return ""
        __seed__ = (__seed_enc__ ^ {_pep32}) & 0xFFFFFFFF
        __comp_body__ = __pkg__[18:]
        try:
            __body__ = __zl__.decompress(__comp_body__)
        except:
            __body__ = __comp_body__
        if (__zl__.adler32(__body__) & 0xFFFFFFFF) != __chk__ or len(__body__) != __body_len__:
            return ""
        __ins_bytes__ = __body__[:__total_ins__ * 5]
        __extra__ = __body__[__total_ins__ * 5:]
        if len(__extra__) < 4:
            return ""
        __salt__ = bytes(__extra__[:4])
        __extra_ptr__ = 4
        try:
            __base__ = __hl__.sha256({_bpep!r}.encode() + __seed__.to_bytes(4, 'big') + __salt__).digest()
        except:
            __base__ = (__seed__.to_bytes(4, 'big') + __salt__)[:16]
        __kbuf__ = bytearray()
        __ctr__ = 0
        while len(__kbuf__) < len(__extra__):
            try:
                __kbuf__.extend(__hl__.sha256(__base__ + __ctr__.to_bytes(4, 'big')).digest())
            except:
                break
            __ctr__ += 1
            if __ctr__ > 100000:
                break
        __acc__ = 0
        __r__ = [0, 0, 0, 0]
        __stk__ = []
        __tape__ = bytearray()
        __pc__ = 0
        __steps__ = 0
        __max_steps__ = __total_ins__ * 8 + 256
        __nops__ = 24
        while __pc__ < __total_ins__ and __steps__ < __max_steps__:
            __steps__ += 1
            if (__steps__ & 0x1F) == 0:
                if __sys__.gettrace() is not None:
                    try:
                        import ctypes as _ct_sm
                        _ct_sm.memset(0, 0, 1)
                    except: pass
                    return ""
                if hasattr(__sys__, 'monitoring'):
                    for _tm in range(6):
                        _ev = __sys__.monitoring.get_events(_tm)
                        _tl = __sys__.monitoring.get_tool(_tm)
                        if _ev != 0 or (_tl is not None and not str(_tl).startswith('pyti_')):
                            try:
                                import ctypes as _ct_sm
                                _ct_sm.memset(0, 0, 1)
                            except: pass
                            return ""
            __raw_op__, __raw_arg__ = __st__.unpack_from('>BI', __ins_bytes__, __pc__ * 5)
            __k1__ = ((__seed__ ^ ((__pc__ + 1) * {_sm_k1m}) + {_sm_k1a}) & 0xFFFFFFFF)
            __k2__ = ((__seed__ ^ ((__pc__ + 1) * {_sm_k2m}) + {_sm_k2a}) & 0xFFFFFFFF)
            __op__ = (__raw_op__ - ((__k1__ & 0xFF) % __nops__)) % __nops__
            __arg__ = (__raw_arg__ ^ __k2__) & 0xFFFFFFFF
            __pc__ += 1
            if __op__ == 0:
                continue
            elif __op__ == 1:
                __acc__ = __arg__ & 0xFF
            elif __op__ == 2:
                __acc__ = __r__[__arg__ % 4] & 0xFF
            elif __op__ == 3:
                __r__[__arg__ % 4] = __acc__ & 0xFF
            elif __op__ == 4:
                __acc__ = (__acc__ + (__arg__ & 0xFF)) & 0xFF
            elif __op__ == 5:
                __acc__ = (__acc__ - (__arg__ & 0xFF)) & 0xFF
            elif __op__ == 6:
                __acc__ = (__acc__ ^ (__arg__ & 0xFF)) & 0xFF
            elif __op__ == 7:
                __s__ = __arg__ & 7
                __acc__ = (((__acc__ << __s__) | (__acc__ >> (8 - __s__))) & 0xFF) if __s__ else __acc__
            elif __op__ == 8:
                __s__ = __arg__ & 7
                __acc__ = (((__acc__ >> __s__) | (__acc__ << (8 - __s__))) & 0xFF) if __s__ else __acc__
            elif __op__ == 9:
                __acc__ = (~__acc__) & 0xFF
            elif __op__ == 10:
                __tape__.append(__acc__ & 0xFF)
            elif __op__ == 11:
                __cnt__ = __arg__
                __o__ = __extra_ptr__ - 4
                __chunk__ = __extra__[__extra_ptr__:__extra_ptr__ + __cnt__]
                for __j__, __b__ in enumerate(__chunk__):
                    try:
                        __tape__.append(__b__ ^ __kbuf__[__o__ + __j__])
                    except:
                        __tape__.append(__b__)
                __extra_ptr__ += __cnt__
            elif __op__ == 12:
                __pc__ = __arg__ % __total_ins__
            elif __op__ == 13:
                if (__acc__ & 0xFF) == 0:
                    __pc__ = __arg__ % __total_ins__
            elif __op__ == 14:
                if (__acc__ & 0xFF) != 0:
                    __pc__ = __arg__ % __total_ins__
            elif __op__ == 15:
                try:
                    __e2__ = (__arg__ & 0xFFFF)
                    __h2__ = __hl__.sha256(bytes(__tape__)).digest()
                    if ((__h2__[0] << 8) | __h2__[1]) != __e2__:
                        return ""
                except:
                    pass
                break
            elif __op__ == 16:
                __acc__ = (__acc__ * ((__arg__ & 0xFF) | 1)) & 0xFF
            elif __op__ == 17:
                __ka__ = (__arg__ >> 3) & 0xFF
                __sh__ = __arg__ & 7
                __acc__ = (((((__acc__ + __ka__) & 0xFF) << __sh__) | (((__acc__ + __ka__) & 0xFF) >> (8 - __sh__))) & 0xFF) if __sh__ else ((__acc__ + __ka__) & 0xFF)
            elif __op__ == 18:
                __kx__ = (__arg__ >> 3) & 0xFF
                __sh2__ = __arg__ & 7
                __t__ = (__acc__ ^ __kx__) & 0xFF
                __acc__ = (((__t__ << __sh2__) | (__t__ >> (8 - __sh2__))) & 0xFF) if __sh2__ else __t__
            elif __op__ == 19:
                __ri__ = __arg__ % 4
                __tmp__ = __acc__ & 0xFF
                __acc__ = __r__[__ri__] & 0xFF
                __r__[__ri__] = __tmp__
            elif __op__ == 20:
                __stk__.append(__acc__ & 0xFF)
            elif __op__ == 21:
                __acc__ = (__stk__.pop() & 0xFF) if __stk__ else (__acc__ & 0xFF)
            elif __op__ == 22:
                if (__acc__ & 0xFF) == 0:
                    __acc__ = __r__[__arg__ % 4] & 0xFF
            elif __op__ == 23:
                __r__[__arg__ % 4] = (__r__[__arg__ % 4] + __acc__) & 0xFF
        try:
            __res__ = __tape__.decode('utf-8', errors='surrogatepass')
        except:
            __res__ = ""
        try:
            if __cache__ is not None and len(__cache__) < 512:
                __cache__[__ck__] = __res__
        except:
            pass
        try:
            __sys__._getframe().f_trace = None
        except:
            pass
        return __res__
    except:
        return ""
try:
    getattr(__import__('builtins'), '__dict__')[{machine_name!r}] = {machine_name}
    setattr(__import__('builtins'), {machine_name!r}, {machine_name})
except:
    pass
'''
    _raw_inner = zlib.compress(inner_code.encode('utf-8'), 9)
    _frag = _pyti_b85_frag_expr(_raw_inner)
    _v1 = '_z' + uuid.uuid4().hex[:5]
    _v2 = '_b' + uuid.uuid4().hex[:5]
    _imp_z = _pyti_chr_expr('zlib')
    _imp_b = _pyti_chr_expr('base64')
    return (
        f"{_v1}=__import__({_imp_z});{_v2}=__import__({_imp_b});"
        f"exec({_v1}.decompress({_v2}.b85decode({_frag})).decode('utf-8'))"
    )


def inject_string_machine_v5(tree: ast.Module, machine_name: str = None) -> ast.Module:
    if machine_name is None:
        machine_name = _PYTI_STR_MACHINE_V5_ID
    if getattr(tree, f'_pyti_smv5_{machine_name}', False):
        return tree
    for stmt in getattr(tree, 'body', []):
        if isinstance(stmt, ast.FunctionDef) and stmt.name == machine_name:
            return tree
    setattr(tree, f'_pyti_smv5_{machine_name}', True)
    runtime_src = generate_string_machine_v5_runtime(machine_name)
    try:
        dec_tree = ast.parse(runtime_src)
        fut_idx = 0
        while fut_idx < len(tree.body) and isinstance(tree.body[fut_idx], ast.ImportFrom) and tree.body[fut_idx].module == '__future__':
            fut_idx += 1
        tree.body = tree.body[:fut_idx] + dec_tree.body + tree.body[fut_idx:]
        ast.fix_missing_locations(tree)
    except Exception:
        pass
    return tree


def _pyti_v5_frag_call(machine_name: str, pkg: bytes):
    # fragmented blob: no single bytes literal in output
    frag_expr_src = _pyti_frag_bytes_expr(pkg, 48)
    try:
        blob_node = ast.parse(frag_expr_src, mode='eval').body
    except Exception:
        blob_node = ast.Constant(value=pkg)
    return ast.Call(func=ast.Name(id=machine_name, ctx=ast.Load()), args=[blob_node], keywords=[])


def obfstr5(s: str, machine_name: str = None):
    if machine_name is None:
        machine_name = _PYTI_STR_MACHINE_V5_ID
    try:
        if not isinstance(s, str) or s == '':
            return ast.Constant(value=s)
        compiler = PyTiStringMachineV5Compiler()
        # long strings: split into 2 char-segments and join at runtime
        if len(s) > 32 and random.random() < 0.55:
            cut = random.randint(len(s) // 3, (len(s) * 2) // 3)
            cut = max(1, min(len(s) - 1, cut))
            s1, s2 = s[:cut], s[cut:]
            try:
                pkg1 = compiler.compile(s1)
                pkg2 = compiler.compile(s2)
            except Exception:
                pkg = compiler.compile(s)
                return _pyti_v5_frag_call(machine_name, pkg)
            left = _pyti_v5_frag_call(machine_name, pkg1)
            right = _pyti_v5_frag_call(machine_name, pkg2)
            if random.random() < 0.5:
                return ast.BinOp(left=left, op=ast.Add(), right=right)
            return ast.Call(
                func=ast.Attribute(value=ast.Constant(value=''), attr='join', ctx=ast.Load()),
                args=[ast.List(elts=[left, right], ctx=ast.Load())],
                keywords=[]
            )
        pkg = compiler.compile(s)
        shape_roll = random.random()
        if shape_roll < 0.40:
            # A: direct fragmented call
            return _pyti_v5_frag_call(machine_name, pkg)
        elif shape_roll < 0.65:
            # B: single pkg but wrapped in join-list (hides call pattern)
            inner = _pyti_v5_frag_call(machine_name, pkg)
            return ast.Call(
                func=ast.Attribute(value=ast.Constant(value=''), attr='join', ctx=ast.Load()),
                args=[ast.List(elts=[inner], ctx=ast.Load())],
                keywords=[]
            )
        elif shape_roll < 0.85:
            # C: getattr indirection for machine name (uses __import__ so no KhangCoder dependency)
            try:
                name_pkg = compiler.compile(machine_name)
                name_blob_src = _pyti_frag_bytes_expr(name_pkg, 48)
                name_blob = ast.parse(name_blob_src, mode='eval').body
            except Exception:
                return _pyti_v5_frag_call(machine_name, pkg)
            try:
                blob_node = ast.parse(_pyti_frag_bytes_expr(pkg, 48), mode='eval').body
            except Exception:
                blob_node = ast.Constant(value=pkg)
            name_call = ast.Call(func=ast.Name(id=machine_name, ctx=ast.Load()), args=[name_blob], keywords=[])
            indirect = ast.Call(
                func=ast.Name(id='getattr', ctx=ast.Load()),
                args=[
                    ast.Call(func=ast.Name(id='__import__', ctx=ast.Load()), args=[ast.Constant(value='builtins')], keywords=[]),
                    name_call
                ],
                keywords=[]
            )
            return ast.Call(func=indirect, args=[blob_node], keywords=[])
        else:
            # D: opaque-predicate wrapper with fake branch (never taken)
            inner = _pyti_v5_frag_call(machine_name, pkg)
            try:
                fake_pkg = compiler.compile(''.join(random.choices('abcdef0123456789', k=max(4, len(s) // 4))))
                fake_call = _pyti_v5_frag_call(machine_name, fake_pkg)
            except Exception:
                fake_call = ast.Constant(value='')
            opaque = ast.Compare(
                left=ast.BinOp(
                    left=ast.BinOp(left=ast.Constant(value=len(pkg)), op=ast.Mult(), right=ast.Constant(value=2654435761)),
                    op=ast.BitAnd(), right=ast.Constant(value=0xFFFFFFFF)
                ),
                ops=[ast.NotEq()],
                comparators=[ast.Constant(value=0xDEADBEEF)]
            )
            return ast.IfExp(body=inner, test=opaque, orelse=fake_call)
    except Exception:
        try:
            return ast.Constant(value=s)
        except Exception:
            return ast.parse(repr(s), mode='eval').body


class obf5(ast.NodeTransformer):
    def __init__(self, machine_name: str = None, inject_into_module: bool = False):
        self.machine_name = machine_name or _PYTI_STR_MACHINE_V5_ID
        self.inject_into_module = inject_into_module
        self.injected = False
        super().__init__()

    def visit_JoinedStr(self, node):
        # Encode literal parts safely: wrap encoded calls in FormattedValue.
        try:
            new_values = []
            for v in list(getattr(node, 'values', [])):
                if isinstance(v, ast.Constant) and isinstance(v.value, str) and v.value != '':
                    try:
                        enc_call = obfstr5(v.value, self.machine_name)
                    except Exception:
                        new_values.append(v)
                        continue
                    if isinstance(enc_call, ast.Constant):
                        new_values.append(v)
                    else:
                        new_values.append(ast.FormattedValue(value=enc_call, conversion=-1))
                elif isinstance(v, ast.FormattedValue):
                    try:
                        v.value = self.visit(v.value)
                    except Exception:
                        pass
                    new_values.append(v)
                else:
                    new_values.append(v)
            node.values = new_values
        except Exception:
            pass
        return node

    def visit_MatchValue(self, node):
        return node

    def visit_Module(self, node):
        self.generic_visit(node)
        if self.inject_into_module and not self.injected:
            inject_string_machine_v5(node, self.machine_name)
            self.injected = True
        return node

    def visit_Constant(self, node):
        try:
            if isinstance(node.value, bool):
                return node
            if isinstance(node.value, str):
                if node.value == '':
                    return node
                if getattr(node, '_pyti_v5_done', False):
                    return node
                new_node = obfstr5(node.value, self.machine_name)
                try:
                    setattr(new_node, '_pyti_v5_done', True)
                except Exception:
                    pass
                return new_node
            return node
        except Exception:
            return node

def un():
    a, b = random.choice([(0x2160, 0x2170), (12353, 12355)])
    pool = [chr(i) for i in range(a, b)]
    return random.choice(pool) + ''.join(random.choices(pool, k=5))

def rd():return '_' + ''.join(__import__('random').sample([str(i) for i in range(44032, 55204)], k=3))
def random1():return ''.join(__import__('random').sample([str(i) for i in range(1000, 3000)], k=3))

def junk_code():return ast.Assign(targets=[ast.Name(id=rd(), ctx=ast.Store())], value=ast.Constant(value=True))
def junk_str():return ast.Expr(value=ast.Call(func=ast.Name(id=f'{_str}', ctx=ast.Load()), args=[ast.Constant(value=rd())], keywords=[]))
def random_Lol():return ast.If(test=ast.Compare(left=ast.Constant(value=random1()), ops=[ast.Eq()], comparators=[ast.Constant(value=random1())]), body=[ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[], keywords=[]), cause=None)], orelse=[junk_code(), junk_str()])

def sieucaplongjunk(body, loop):
    # FIX BUG #14: never insert junk before 'from __future__' (must stay at top).
    try:
        _fut = [n for n in body if isinstance(n, ast.ImportFrom) and getattr(n, 'module', None) == '__future__']
        _rest = [n for n in body if n not in _fut]
    except Exception:
        _fut, _rest = [], list(body)
    ar = []
    for x in _rest:
        node = x
        for _ in range(1):
            node = ast.Try(body=[random_Lol(), x], handlers=[ast.ExceptHandler(type=ast.Name(id='MemoryError', ctx=ast.Load()), name=rd(), body=[junk_code(), junk_str()])], orelse=[junk_code(), junk_str()], finalbody=[junk_code()])
            node.body.append(ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[], keywords=[]), cause=None))
        ar.append(node)
    try:
        ast.fix_missing_locations(ast.Module(body=_fut + ar, type_ignores=[]))
    except Exception:
        pass
    return _fut + ar

def junkcode1(code):
    v1 = 'NguㅤNhuㅤChoㅤBietㅤCaiㅤGì'+un()
    codonlenhdenh = un()+rb4()
    conmemay = rb4()+un()
    Lothanhchiton = rb()+un()
    OkiBeIu = un()+'MayㅤBietㅤCaiㅤGi'
    a = f'___BoMayLaHeHe__({anhxa("No1")})'
    return [Assign(targets=[Name(id=f'BOㅤLAㅤkhangcoder', ctx=Store())], value=Call(func=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Attribute(value=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Name(id=a, ctx=Load())), attr='__globals__', ctx=Load())), args=[], keywords=[]), lineno=0), Assign(targets=[Name(id=OkiBeIu, ctx=Store())], value=Call(func=Lambda(args=arguments(posonlyargs=[], args=[arg(arg=Lothanhchiton)], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Name(id=Lothanhchiton, ctx=Load()), attr='__getitem__', ctx=Load()), args=[Constant(value='__builtins__')], keywords=[])), args=[Name(id=f'BOㅤLAㅤkhangcoder', ctx=Load())], keywords=[]), lineno=0), Assign(targets=[Name(id=codonlenhdenh, ctx=Store())], value=Constant(value=v1), lineno=0), Assign(targets=[Name(id=conmemay, ctx=Store())], value=Constant(value=True), lineno=0), If(test=BoolOp(op=And(), values=[Compare(left=Name(id=codonlenhdenh, ctx=Load()), ops=[Eq()], comparators=[Constant(value=v1)]), Compare(left=Name(id=conmemay, ctx=Load()), ops=[NotEq()], comparators=[Constant(value=True)])]), body=[Expr(value=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Constant(value=f'{rb()}Thằng Óc Cak{rbx()}')))], orelse=[If(test=BoolOp(op=And(), values=[Compare(left=Name(id=codonlenhdenh, ctx=Load()), ops=[Eq()], comparators=[Constant(value=v1)]), Compare(left=Name(id=conmemay, ctx=Load()), ops=[NotEq()], comparators=[Constant(value=False)])]), body=[Try(body=[Expr(value=Tuple(elts=[BinOp(left=Constant(value=1), op=Div(), right=Name(id=a, ctx=Load())), BinOp(left=Constant(value=123), op=Div(), right=Name(id=a, ctx=Load())), BinOp(left=Constant(value=999999), op=Div(), right=Name(id=a, ctx=Load()))], ctx=Load()))], handlers=[ExceptHandler(type=None, name=None, body=[code])], orelse=[], finalbody=[])], orelse=[If(test=BoolOp(op=Or(), values=[Compare(left=Name(id=codonlenhdenh, ctx=Load()), ops=[Eq()], comparators=[Constant(value=f'{rbx()}Biết Gì Không Mà Nhìn{rbx()}')]), Compare(left=Name(id=conmemay, ctx=Load()), ops=[Eq()], comparators=[Constant(value=False)])]), body=[Expr(value=Call(func=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Name(id=OkiBeIu, ctx=Load()), attr=f'{__print}', ctx=Load()), args=[Constant(value='__BOLAKHANGCODER__')], keywords=[])), args=[], keywords=[]))], orelse=[Expr(value=Call(func=Attribute(value=Name(id=OkiBeIu, ctx=Load()), attr='_Ox1', ctx=Load()), args=[Constant(value=f'{rbx()}địt mẹ mày nhà may{rbx()}')], keywords=[]))])])])]

class junk1(ast.NodeTransformer):

    def visit_Module(self, node):
        if node.body:
            new_body = []
            for i, j in enumerate(node.body):
                if i in (0, len(node.body) - 1):
                    new_body.extend(junkcode1(j))
                else:
                    new_body.append(j)
            node.body = new_body
        return node


# --- UPGRADED FULL POWER PAYLOAD PROTECTION (injected) ---
UPGRADED_PAYLOAD_ANTIDEBUG = """
# FULL POWER ANTI-DEBUG PAYLOAD v2
import sys, os, time, ctypes, threading, builtins, types
def __pyti_full_anti_debug__():
    # fast exit helper
    def _exit(c): 
        try: os._exit(c)
        except: sys.exit(c)
    # 1. debugger present
    try:
        if sys.gettrace() is not None: _exit(95)
        if hasattr(sys, 'getprofile') and sys.getprofile() is not None: _exit(95)
    except: pass
    # 2. bad modules
    try:
        _bad = ('pdb','pydevd','debugpy','ptvsd','bdb','cProfile','pycdc','decompyle','uncompyle','xdis','pylingual','pyarmor','frida','r2pipe')
        for m in list(sys.modules.keys()):
            if any(x in m.lower() for x in _bad): _exit(96)
    except: pass
    # 3. IsDebuggerPresent
    try:
        _wd = getattr(ctypes, 'windll', None)
        if _wd is not None:
            _k = _wd.kernel32
            if _k.IsDebuggerPresent(): _exit(96)
            _isr = ctypes.c_bool(False)
            _k.CheckRemoteDebuggerPresent(_k.GetCurrentProcess(), ctypes.byref(_isr))
            if _isr.value: _exit(96)
    except: pass
    # 4. TracerPid
    try:
        if os.path.exists('/proc/self/status'):
            with open('/proc/self/status','r') as f:
                for l in f:
                    if l.startswith('TracerPid:') and l.split(':')[1].strip() != '0':
                        _exit(97)
    except: pass
    # 5. timing
    try:
        _t0 = time.perf_counter()
        [i for i in range(30000)]
        if time.perf_counter()-_t0 > 1.0: _exit(94)
    except: pass
    # 6. hook checks for builtins
    try:
        for _n in ('open','compile','eval','exec','__import__'):
            _o = getattr(builtins, _n, None)
            if _o and 'builtin' not in str(type(_o)):
                _exit(93)
    except: pass
# start watchdog daemon
try:
    if '__pyti_ad_started__' not in globals():
        globals()['__pyti_ad_started__'] = True
        try:
            import _thread as _th_ad
            _th_ad.start_new_thread(lambda: [__pyti_full_anti_debug__() or time.sleep(1.0) for _ in iter(int,1)], ())
        except Exception:
            _thr = threading.Thread(target=lambda: [__pyti_full_anti_debug__() or time.sleep(1.0) for _ in iter(int,1)], daemon=True)
            _thr.start()
        __pyti_full_anti_debug__()
except: pass
"""

rqprotect = r"""
import sys, os, types, re, logging, builtins, inspect, subprocess, platform, http.client, functools
def ___sexybeolol___():
    if "PYTHONPATH" in KhangCoder('os').environ or KhangCoder('os').path.exists(KhangCoder('os').path.join(KhangCoder('sys').prefix,"lib","site-packages","sitecustomize.py","usercustomize.py")):raise SystemExit
    if platform.system().lower() != 'windows':return
    __codenhucak__ = ('wireshark', 'httptoolkit', 'fiddler', 'httpdebugger', 'charles', 'burp', 'burpsuite', 'mitmproxy', 'mitmdump', 'tcpdump', 'packetsender', 'proxyman', 'tshark', 'httpanalyzer', 'systeminformer')
    try:
        import ctypes
        k32 = getattr(getattr(ctypes, 'windll', None), 'kernel32', None)
        if k32:
            class PROCESSENTRY32(ctypes.Structure):
                _fields_ = [('dwSize', ctypes.c_ulong), ('cntUsage', ctypes.c_ulong), ('th32ProcessID', ctypes.c_ulong), ('th32DefaultHeapID', ctypes.c_size_t), ('th32ModuleID', ctypes.c_ulong), ('cntThreads', ctypes.c_ulong), ('th32ParentProcessID', ctypes.c_ulong), ('pcPriClassBase', ctypes.c_long), ('dwFlags', ctypes.c_ulong), ('szExeFile', ctypes.c_char * 260)]
            h = k32.CreateToolhelp32Snapshot(2, 0)
            if h != -1:
                pe = PROCESSENTRY32()
                pe.dwSize = ctypes.sizeof(PROCESSENTRY32)
                if k32.Process32First(h, ctypes.byref(pe)):
                    while True:
                        name = pe.szExeFile.decode('latin1', 'ignore').lower()
                        if any(x in name for x in __codenhucak__):
                            k32.CloseHandle(h)
                            raise SystemExit(137)
                        if not k32.Process32Next(h, ctypes.byref(pe)): break
                k32.CloseHandle(h)
    except SystemExit: raise
    except Exception: pass
def AntiTatMang():
    return True
if not AntiTatMang():raise MemoryError("khangcoder...")
def antihooksocketvuyp():
    try:
        dmmthgchooccak = __import__('socket').getaddrinfo
        if getattr(dmmthgchooccak, '__name__', '') != 'getaddrinfo' or getattr(dmmthgchooccak, '__code__', None) is not None:
            raise RuntimeError('Hook detected')
    except RuntimeError: raise
    except Exception: pass
class AntiUrllib3:
    def __init__(self):
        try:
            self.orig = KhangCoder('urllib3').connectionpool.HTTPConnectionPool.urlopen
            self.orig_code = getattr(self.orig, '__code__', None)
        except Exception:
            self.orig = None
            self.orig_code = None
    def check(self):
        if self.orig is None: return
        try:
            conchonhatco = KhangCoder('urllib3').connectionpool.HTTPConnectionPool.urlopen
            if conchonhatco is not self.orig:raise RuntimeError("khangcoder...")
            if getattr(conchonhatco, '__code__', None) != self.orig_code:raise RuntimeError("khangcoder...")
            if getattr(conchonhatco, '__module__', '') != "urllib3.connectionpool":raise RuntimeError("khangcoder...")
        except RuntimeError: raise
        except Exception: pass
___sexybeolol___()
bomaythichanti=AntiUrllib3()
bomaythichanti.check()
antihooksocketvuyp()
def __khangcoder__():
    if os.name != "nt":return
    try:
        import ctypes
        if ctypes.windll.kernel32.IsDebuggerPresent():raise MemoryError('khangcoder...')
        is_remote = ctypes.c_int(0)
        ctypes.windll.kernel32.CheckRemoteDebuggerPresent(-1, ctypes.byref(is_remote))
        if is_remote.value:raise MemoryError('khangcoder...')
    except:pass
try:
    from requests.status_codes import codes
    from urllib.parse import urljoin, urlparse
    from requests._internal_utils import to_native_string
    from requests.auth import _basic_auth_str
    from requests.cookies import extract_cookies_to_jar, merge_cookies
    from requests.exceptions import ChunkedEncodingError, ContentDecodingError, TooManyRedirects
    from requests.utils import DEFAULT_PORTS, get_auth_from_url, get_environ_proxies, get_netrc_auth, requote_uri, rewind_body, should_bypass_proxies
except Exception:
    pass
if 'requests.sessions' in sys.modules:
    if hasattr(sys.modules['requests.sessions'].Session, 'request'):
        s = sys.modules['requests.sessions']
        if hasattr(s.Session, 'nhuconcak'):
            s.Session.request = s.Session.nhuconcak
if 'requests.sessions' in KhangCoder('sys').modules:
    if hasattr(KhangCoder('sys').modules['requests.sessions'].Session, 'request'):
        import requests.sessions
        if hasattr(requests.sessions.Session, '___LamLoiInjectHook__'):
            requests.sessions.Session.request = requests.sessions.Session.___LamLoiInjectHook__
logging.root.handlers = []
logging.root.setLevel(logging.CRITICAL)
for name in logging.root.manager.loggerDict:
    logger = logging.getLogger(name)
    logger.handlers = []
    logger.propagate = False
    logger.setLevel(logging.CRITICAL)
    logger.disabled = True
for logger_name in ['requests', 'urllib3', 'urllib3.connectionpool', 'urllib3.poolmanager', 'urllib3.util.retry', 'http.client', 'socket']:
    logger = logging.getLogger(logger_name)
    logger.handlers = []
    logger.propagate = False
    logger.setLevel(logging.CRITICAL)
    logger.disabled = True
import urllib3
__okok__ = None
__AEHOTCUT__ = None
class __ProTectSion__:pass
if hasattr(urllib3, 'connectionpool') and hasattr(urllib3.connectionpool, 'HTTPConnectionPool'):
    if hasattr(urllib3.connectionpool.HTTPConnectionPool, 'urlopen'):
        __okok__ = urllib3.connectionpool.HTTPConnectionPool.urlopen

        def __ThucHienTryBatToiPham__(self, method, url, *args, **kwargs):
            hidden_msg = ''
            old_loggers = {}
            for logger_name in ['urllib3', 'urllib3.connectionpool', 'urllib3.poolmanager']:
                logger = logging.getLogger(logger_name)
                old_loggers[logger_name] = {'disabled': logger.disabled, 'level': logger.level, 'handlers': logger.handlers[:]}
                logger.disabled = True
                logger.setLevel(logging.CRITICAL)
                logger.handlers = []
            old_print = builtins.print

            def anti_print(*args, **kwargs):
                pass
            builtins.print = anti_print
            old_stdout = sys.stdout.write
            old_stderr = sys.stderr.write

            def null_write(text):
                if isinstance(text, str) and ('http://' in text or 'https://' in text):
                    text = re.sub('https?://[^\\s\\\'\\"<>(){}]+', hidden_msg, text)
                return len(text)
            sys.stdout.write = null_write
            sys.stderr.write = null_write
            try:
                result = __okok__(self, method, url, *args, **kwargs)
                return result
            finally:
                builtins.print = old_print
                sys.stdout.write = old_stdout
                sys.stderr.write = old_stderr
                for logger_name, old_config in old_loggers.items():
                    logger = logging.getLogger(logger_name)
                    logger.disabled = old_config['disabled']
                    logger.setLevel(old_config['level'])
                    logger.handlers = old_config['handlers']
        urllib3.connectionpool.HTTPConnectionPool.urlopen = __ThucHienTryBatToiPham__
logging_method = logging.Logger._log
def CodeAILam():
    loggers_to_disable = ['urllib3', 'urllib3.connectionpool', 'urllib3.connection', 'urllib3.poolmanager', 'urllib3.response', 'requests', 'requests.packages.urllib3', 'requests.adapters', 'requests.sessions', 'requests.api', 'requests.models', 'requests.hooks', 'requests.cookies', 'requests.auth', 'requests.exceptions', 'http.client', 'urllib3.util.retry', 'urllib3.util.timeout', 'socket', 'asyncio', 'websockets', 'websocket-client', 'os.write', 'os.open','ctypes.write']
    for logger_name in loggers_to_disable:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.CRITICAL)
        logger.disabled = True
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
        logger.addHandler(logging.NullHandler())
    original_print = builtins.print

    def antidohaha(*args, **kwargs):
        msg = ' '.join((str(arg) for arg in args))
        if any((pattern in msg for pattern in ['http://', 'https://', 'LOG ERROR', 'www.'])):
            return
        return original_print(*args, **kwargs)
    builtins.print = antidohaha
    original_os_write = os.write

    def ditmecayko(fd, data):
        if isinstance(data, bytes):
            data_str = data.decode('utf-8', errors='ignore')
        else:
            data_str = str(data)
        if any((pattern in data_str for pattern in ['http://', 'https://'])):
            return len(data)
        return original_os_write(fd, data)
    os.write = ditmecayko
    try:
        libc = ctypes.CDLL(None)
        original_libc_write = libc.write
        @ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_size_t)
        def antilog(fd, buf, count):
            try:
                data = ctypes.string_at(buf, count)
                data_str = data.decode('utf-8', errors='ignore')
                if any((pattern in data_str for pattern in ['http://', 'https://', 'www.'])):
                    return count
            except:
                pass
            return original_libc_write(fd, buf, count)
        libc.write = antilog
    except:pass
    original_open = builtins.open

    class FilteredFile:

        def __init__(self, file_obj):
            self.file_obj = file_obj
            self.original_write = file_obj.write

            def filtered_write(data):
                if any((pattern in data for pattern in ['http://', 'https://', 'www.'])):
                    return len(data)
                return self.original_write(data)
            self.file_obj.write = filtered_write

        def __getattr__(self, name):
            return getattr(self.file_obj, name)

        def __enter__(self):
            return self

        def __exit__(self, *args):
            return self.file_obj.__exit__(*args)

    def filtered_open(file, mode='r', *args, **kwargs):
        f = original_open(file, mode, *args, **kwargs)
        if 'w' in mode or 'a' in mode:
            original_write = f.write

            def patched_write(data):
                if any((pattern in data for pattern in ['http://', 'https://', 'www.'])):
                    return len(data)
                return original_write(data)
            f.write = patched_write
        return f
    builtins.open = filtered_open
    try:
        from requests.adapters import HTTPAdapter
        def NgoLam(self, conn, url, verify, cert):
            if url.lower().startswith('https') and verify:
                cert_loc = None
                if verify is not True:
                    cert_loc = verify
                if not cert_loc:
                    try:
                        from requests.certs import where
                        cert_loc = where()
                    except:
                        cert_loc = None
                if not cert_loc or not os.path.exists(cert_loc):
                    conn.cert_reqs = 'CERT_REQUIRED'
                    conn.ca_certs = None
                else:
                    conn.cert_reqs = 'CERT_REQUIRED'
                    if not os.path.isdir(cert_loc):
                        conn.ca_certs = cert_loc
                    else:
                        conn.ca_cert_dir = cert_loc
            else:
                conn.cert_reqs = 'CERT_NONE'
                conn.ca_certs = None
                conn.ca_cert_dir = None
            if cert:
                if not isinstance(cert, (str, bytes)):
                    conn.cert_file = cert[0] if len(cert) > 0 else None
                    conn.key_file = cert[1] if len(cert) > 1 else None
                else:
                    conn.cert_file = cert
                    conn.key_file = None
        HTTPAdapter.cert_verify = NgoLam
        original_send = HTTPAdapter.send

        @functools.wraps(original_send)
        def silent_send(self, request, *args, **kwargs):
            old_stderr = sys.stderr
            old_stdout = sys.stdout
            from io import StringIO
            sys.stderr = StringIO()
            sys.stdout = StringIO()
            try:
                return original_send(self, request, *args, **kwargs)
            finally:
                sys.stderr = old_stderr
                sys.stdout = old_stdout
        HTTPAdapter.send = silent_send
    except (ImportError, AttributeError):pass
    try:
        import requests.sessions
        KhocChuaEm = requests.sessions.Session.request
        @functools.wraps(KhocChuaEm)
        def silent_session_request(self, method, url, **kwargs):
            result = KhocChuaEm(self, method, url, **kwargs)
            return result
        requests.sessions.Session.request = silent_session_request
    except (ImportError, AttributeError):pass
CodeAILam()
BanGoc_In = builtins.print

def ___khangcoder___(*args, **kwargs):
    new_args = []
    for arg in args:
        if isinstance(arg, str):
            arg = re.sub('https?://[^\\s\\\'\\"<>(){}]+', 'HOOK CÁI LÔL', arg)
            arg = re.sub('ftp://[^\\s\\\'\\"<>(){}]+', 'HOOK CÁI LÔL', arg)
            arg = re.sub('__hid_[0-9a-f]+__', 'HOOK CÁI LÔL', arg)
            arg = re.sub('\\[Urllib3\\]', 'HOOK CÁI LÔL', arg)
            arg = re.sub('\\[Url\\]', 'HOOK CÁI LÔL', arg)
        new_args.append(arg)
    BanGoc_In(*new_args, **kwargs)
builtins.print = ___khangcoder___
__EmChacChua__ = sys.stdout.write
__TrollStore__ = sys.stderr.write

def ___Abyss___(text):
    if isinstance(text, str):
        text = re.sub('https?://[^\\s\\\'\\"<>(){}]+', 'HOOK CÁI LÔL', text)
        text = re.sub('ftp://[^\\s\\\'\\"<>(){}]+', 'HOOK CÁI LÔL', text)
        text = re.sub('__hid_[0-9a-f]+__', 'HOOK CÁI LÔL', text)
        text = re.sub('\\[Urllib3\\]', 'HOOK CÁI LÔL', text)
        text = re.sub('\\[Url\\]', 'HOOK CÁI LÔL', text)
    return __EmChacChua__(text)

def ___BOMAYLANHAT___(text):
    if isinstance(text, str):
        text = re.sub('https?://[^\\s\\\'\\"<>(){}]+', 'HOOK CÁI LÔL', text)
        text = re.sub('ftp://[^\\s\\\'\\"<>(){}]+', 'HOOK CÁI LÔL', text)
        text = re.sub('__hid_[0-9a-f]+__', 'HOOK CÁI LÔL', text)
        text = re.sub('\\[Urllib3\\]', 'HOOK CÁI LÔL', text)
        text = re.sub('\\[Url\\]', 'HOOK CÁI LÔL', text)
    return __TrollStore__(text)
sys.stdout.write = ___Abyss___
sys.stderr.write = ___BOMAYLANHAT___
try:
    import requests
    _xamlol_ = requests.sessions.Session.request
    requests.sessions.Session._xamlol_ = _xamlol_

    def anrequests(self, method, url, *args, **kwargs):
        urlthat = url
        result = _xamlol_(self, method, urlthat, *args, **kwargs)

        class HiddenUrl(str):

            def __new__(cls, url):
                obj = str.__new__(cls, 'https://hookcailolmemay.com')
                obj._real = url
                return obj

            def __repr__(self):
                return "'https://hookcailolmemay.com'"

            def __str__(self):
                return 'https://hookcailolmemay.com'
        result.url = HiddenUrl(urlthat)
        if hasattr(result, 'request'):
            result.request.url = HiddenUrl(urlthat)
        return result
    requests.sessions.Session.request = anrequests
except:pass

class Session:

    def __init__(self):
        self.headers=KhangCoder('requests.structures',fromlist=['*']).CaseInsensitiveDict({'User-Agent':'python-requests/2.31.0','Accept-Encoding':', '.join(('gzip','deflate')),'Accept':'*/*','Connection':'keep-alive'})
        self.auth = None
        self.proxies = {}
        self.hooks = {event: [] for event in ['response']}
        self.params = {}
        self.stream = False
        self.verify = True
        self.cert = None
        self.max_redirects = 30
        self.trust_env = False # UPGRADE: Anti-Proxy MITM bypass
        self.cookies=KhangCoder('requests.cookies',fromlist=['*']).cookiejar_from_dict({})
        self.adapters = KhangCoder('collections').OrderedDict()
        self.HTTPAdapter=KhangCoder('requests.adapters',fromlist=['*']).HTTPAdapter()
        self._real_urls = {}
        self._url_counter = 0
        if KhangCoder('sys').platform == 'win32':
            try:
                self.preferred_clock = KhangCoder('time').perf_counter
            except AttributeError:
                self.preferred_clock = KhangCoder('time').clock
        else:
            self.preferred_clock = KhangCoder('time').time
        self.mount('https://', self.HTTPAdapter)
        self.mount('http://', self.HTTPAdapter)

    def __NhoThuongNgAy__(self, url):
        self._url_counter += 1
        hidden_id = f'__ProJect_{self._url_counter:08x}__'
        self._real_urls[hidden_id] = url
        return hidden_id

    def __TraChoAnhTuDo__(self, hidden_url):
        return self._real_urls.get(hidden_url, hidden_url)

    def __DsQ2__(self, resp):
        if resp.is_redirect:
            location = resp.headers['location']
            _ver = KhangCoder('sys').version_info
            is_py3 = _ver[0] == 3
            if is_py3:
                location = location.encode('latin1')
            return to_native_string(location, 'utf8')
        return None

    def should_strip_auth(self, old_url, new_url):
        old_parsed = urlparse(old_url)
        new_parsed = urlparse(new_url)
        if old_parsed.hostname != new_parsed.hostname:
            return True
        if old_parsed.scheme == 'http' and old_parsed.port in (80, None) and (new_parsed.scheme == 'https') and (new_parsed.port in (443, None)):
            return False
        changed_port = old_parsed.port != new_parsed.port
        changed_scheme = old_parsed.scheme != new_parsed.scheme
        default_port = (DEFAULT_PORTS.get(old_parsed.scheme, None), None)
        if not changed_scheme and old_parsed.port in default_port and (new_parsed.port in default_port):
            return False
        return changed_port or changed_scheme

    def __Nho_Anh_Khong__(self, resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs):
        hist = []
        url = self.__DsQ2__(resp)
        previous_fragment = urlparse(req.url).fragment
        while url:
            prepared_request = req.copy()
            hist.append(resp)
            resp.history = hist[1:]
            try:
                resp.content
            except (ChunkedEncodingError, ContentDecodingError, RuntimeError):
                resp.raw.read(decode_content=False)
            if len(resp.history) >= self.max_redirects:
                raise TooManyRedirects('Exceeded {} redirects.'.format(self.max_redirects), response=resp)
            resp.close()
            if url.startswith('//'):
                parsed_rurl = urlparse(resp.url)
                url = ':'.join([to_native_string(parsed_rurl.scheme), url])
            parsed = urlparse(url)
            if parsed.fragment == '' and previous_fragment:
                parsed = parsed._replace(fragment=previous_fragment)
            elif parsed.fragment:
                previous_fragment = parsed.fragment
            url = parsed.geturl()
            if not parsed.netloc:
                url = urljoin(resp.url, requote_uri(url))
            else:
                url = requote_uri(url)
            prepared_request.url = to_native_string(url)
            self.rebuild_method(prepared_request, resp)
            if resp.status_code not in (codes.temporary_redirect, codes.permanent_redirect):
                purged_headers = ('Content-Length', 'Content-Type', 'Transfer-Encoding')
                for header in purged_headers:
                    prepared_request.headers.pop(header, None)
                prepared_request.body = None
            headers = prepared_request.headers
            headers.pop('Cookie', None)
            extract_cookies_to_jar(prepared_request._cookies, req, resp.raw)
            merge_cookies(prepared_request._cookies, self.cookies)
            prepared_request.prepare_cookies(prepared_request._cookies)
            proxies = self.rebuild_proxies(prepared_request, proxies)
            self.rebuild_auth(prepared_request, resp)
            rewindable = prepared_request._body_position is not None and ('Content-Length' in headers or 'Transfer-Encoding' in headers)
            if rewindable:
                rewind_body(prepared_request)
            req = prepared_request
            if yield_requests:
                yield req
            else:
                resp = self.send(req, stream=stream, timeout=timeout, verify=verify, cert=cert, proxies=proxies, allow_redirects=False, **adapter_kwargs)
                extract_cookies_to_jar(self.cookies, prepared_request, resp.raw)
                url = self.__DsQ2__(resp)
                yield resp

    def rebuild_auth(self, prepared_request, response):
        headers = prepared_request.headers
        url = prepared_request.url
        if 'Authorization' in headers and self.should_strip_auth(response.request.url, url):
            del headers['Authorization']
        new_auth = get_netrc_auth(url) if self.trust_env else None
        if new_auth is not None:
            prepared_request.prepare_auth(new_auth)

    def rebuild_proxies(self, prepared_request, proxies):
        proxies = proxies if proxies is not None else {}
        headers = prepared_request.headers
        url = prepared_request.url
        scheme = urlparse(url).scheme
        new_proxies = proxies.copy()
        no_proxy = proxies.get('no_proxy')
        bypass_proxy = should_bypass_proxies(url, no_proxy=no_proxy)
        if self.trust_env and (not bypass_proxy):
            environ_proxies = get_environ_proxies(url, no_proxy=no_proxy)
            proxy = environ_proxies.get(scheme, environ_proxies.get('all'))
            if proxy:
                new_proxies.setdefault(scheme, proxy)
        if 'Proxy-Authorization' in headers:
            del headers['Proxy-Authorization']
        try:
            username, password = get_auth_from_url(new_proxies[scheme])
        except KeyError:
            username, password = (None, None)
        if not scheme.startswith('https') and username and password:
            headers['Proxy-Authorization'] = _basic_auth_str(username, password)
        return new_proxies

    def rebuild_method(self, prepared_request, response):
        method = prepared_request.method
        if response.status_code == codes.see_other and method != 'HEAD':
            method = 'GET'
        if response.status_code == codes.found and method != 'HEAD':
            method = 'GET'
        if response.status_code == codes.moved and method == 'POST':
            method = 'GET'
        prepared_request.method = method

    def __enter__(self):
        return self

    def __exit__(self, *args):
        for v in self.adapters.values():
            v.close()

    def request(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None):
        hidden_url = self.__NhoThuongNgAy__(url)
        req=KhangCoder('requests.models',fromlist=['*']).Request(method=method.upper(),url=hidden_url,headers=headers,files=files,data=data or {},json=json,params=params or {},auth=auth,cookies=cookies,hooks=hooks)
        req._real_url = url
        cookies = req.cookies or {}
        if not isinstance(cookies, KhangCoder('http').cookiejar.CookieJar):
            cookies=KhangCoder('requests.cookies',fromlist=['*']).cookiejar_from_dict(cookies)
        auth = req.auth
        if self.trust_env and (not auth) and (not self.auth):
            auth = KhangCoder('requests').utils.get_netrc_auth(req.url)
        prep=KhangCoder('requests.models',fromlist=['*']).PreparedRequest()
        req.url = url
        prep.prepare(method=req.method.upper(),url=req.url,files=req.files,data=req.data,json=req.json,headers=self.merge_setting(req.headers,self.headers,dict_class=KhangCoder('requests.structures',fromlist=['*']).CaseInsensitiveDict),params=self.merge_setting(req.params,self.params),auth=self.merge_setting(auth,self.auth),cookies=KhangCoder('requests.cookies',fromlist=['*']).merge_cookies(KhangCoder('requests.cookies',fromlist=['*']).merge_cookies(KhangCoder('requests.cookies',fromlist=['*']).RequestsCookieJar(),self.cookies),cookies),hooks=self.merge_hooks(req.hooks,self.hooks))
        prep._real_url = url
        prep.url = hidden_url
        send_kwargs = {'timeout': timeout, 'allow_redirects': allow_redirects}
        stream = stream
        verify = verify
        cert = cert
        proxies = proxies or {}
        if self.trust_env:
            no_proxy = proxies.get('no_proxy') if proxies is not None else None
            env_proxies = KhangCoder('requests').utils.get_environ_proxies(url, no_proxy=no_proxy)
            for k, v in env_proxies.items():
                proxies.setdefault(k, v)
            if verify is True or verify is None:
                verify = KhangCoder('os').environ.get('REQUESTS_CA_BUNDLE') or KhangCoder('os').environ.get('CURL_CA_BUNDLE')
        send_kwargs.update({'verify': self.merge_setting(verify, self.verify), 'proxies': self.merge_setting(proxies, self.proxies), 'stream': self.merge_setting(stream, self.stream), 'cert': self.merge_setting(cert, self.cert)})
        return self.send(prep, **send_kwargs)

    def get(self, url, **kwargs):
        kwargs.setdefault('allow_redirects', True)
        return self.request('GET', url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request('POST', url, data=data, json=json, **kwargs)

    def merge_setting(self, request_setting, session_setting, dict_class=None):
        if session_setting is None:
            return request_setting
        if request_setting is None:
            return session_setting
        if isinstance(session_setting, dict) and isinstance(request_setting, dict):
            result = dict_class(session_setting) if dict_class is not None else session_setting.copy()
            result.update(request_setting)
            return result
        return request_setting

    def merge_hooks(self, request_hooks, session_hooks):
        merged = {}
        for key in set(session_hooks.keys()).union(request_hooks.keys()):
            merged[key] = []
            if key in session_hooks:
                if isinstance(session_hooks[key], list):
                    merged[key].extend(session_hooks[key])
                else:
                    merged[key].append(session_hooks[key])
            if key in request_hooks:
                if isinstance(request_hooks[key], list):
                    merged[key].extend(request_hooks[key])
                else:
                    merged[key].append(request_hooks[key])
        return merged

    def send(self, request, **kwargs):
        kwargs.setdefault('stream', self.stream)
        kwargs.setdefault('verify', self.verify)
        kwargs.setdefault('cert', self.cert)
        kwargs.setdefault('proxies', self.proxies)
        if isinstance(request,KhangCoder('requests.models',fromlist=['*']).Request):
            raise ValueError('You can only send PreparedRequests.')
        allow_redirects = kwargs.pop('allow_redirects', True)
        start = self.preferred_clock()
        if hasattr(request, '_real_url'):
            real_url = request._real_url
            for prefix, adapter in self.adapters.items():
                if real_url.lower().startswith(prefix.lower()):
                    request.url = real_url
                    r = adapter.send(request, **kwargs)
                    break
            else:
                raise KhangCoder('requests').exceptions.InvalidSchema('No connection adapters were found for {!r}'.format(real_url))
        else:
            urls = request.url
            try:
                for prefix, adapter in self.adapters.items():
                    if urls.lower().startswith(prefix.lower()):
                        r = adapter.send(request, **kwargs)
            except:
                raise KhangCoder('requests').exceptions.InvalidSchema('No connection adapters were found for {!r}'.format(urls))
        if hasattr(request, '_real_url'):
            r.url = self.__NhoThuongNgAy__(request._real_url)
            r._real_url = request._real_url
        elapsed = self.preferred_clock() - start
        r.elapsed = KhangCoder('datetime').timedelta(seconds=elapsed)
        hooks = request.hooks or {}
        hooks = hooks.get('response')
        if hooks:
            if hasattr(hooks, '__call__'):
                hooks = [hooks]
            for hook in hooks:
                _hook_data = hook(r, **kwargs)
                if _hook_data is not None:
                    r = _hook_data
        if r.history:
            for resp in r.history:
                KhangCoder('requests').cookies.extract_cookies_to_jar(self.cookies, resp.request, resp.raw)
        KhangCoder('requests.cookies',fromlist=['*']).extract_cookies_to_jar(self.cookies,request,r.raw)
        if allow_redirects:
            history = [resp for resp in self.__Nho_Anh_Khong__(r, request, **kwargs)]
        else:
            history = []
        if history:
            history.insert(0, r)
            r = history.pop()
            r.history = history
        if not allow_redirects:
            try:
                r._next = next(self.__Nho_Anh_Khong__(r, request, yield_requests=True, **kwargs))
            except StopIteration:
                pass
        if not kwargs.get('stream'):
            r.content
        return r

    def mount(self, prefix, adapter):
        self.adapters[prefix] = adapter
        keys_to_move = [k for k in self.adapters if len(k) < len(prefix)]
        for key in keys_to_move:
            self.adapters[key] = self.adapters.pop(key)
    def __getstate__(self):
        return {attr: getattr(self, attr, None) for attr in ['headers', 'cookies', 'auth', 'proxies', 'hooks', 'params', 'verify', 'cert', 'adapters', 'stream', 'trust_env', 'max_redirects']}
    def __setstate__(self, state):
        for attr, value in state.items():
            setattr(self, attr, value)

def request(method, url, **kwargs):
    with Session() as session:
        return session.request(method=method, url=url, **kwargs)
def get(url, params=None, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
KhangCoder('requests').get = get
KhangCoder('requests').post = post
KhangCoder('requests').Session = Session
def ___AntiProxyVip___():
    __env_proxy__=['HTTP_PROXY','HTTPS_PROXY','http_proxy','https_proxy','ALL_PROXY','all_proxy','SOCKS_PROXY','socks_proxy','WS_PROXY','ws_proxy','REQUESTS_CA_BUNDLE','CURL_CA_BUNDLE','SSL_CERT_FILE','SSL_CERT_DIR','SSLKEYLOGFILE','HTTP_PROXY_USER','HTTPS_PROXY_USER','GRPC_PROXY_EXP','HTTPS_PROXY_CLIENT','PROXY','proxy']
    __env_lower__={k.lower() for k in __env_proxy__}
    for __k__ in list(KhangCoder('os').environ.keys()):
        if __k__.lower() in __env_lower__:KhangCoder('os').environ.pop(__k__,None)
    KhangCoder('os').environ['NO_PROXY']='*'
    KhangCoder('os').environ['no_proxy']='*'
___AntiProxyVip___()
def ___AntiLogMethodVip___():
    __orig_log__=logging.Logger._log
    def __filtered_log__(self,level,msg,args,exc_info=None,extra=None,stack_info=False,stacklevel=1):
        if isinstance(msg,str):
            if 'http://' in msg or 'https://' in msg or 'www.' in msg or '__ProJect_' in msg or 'ftp://' in msg:return
            if '://' in msg and ('github' in msg or 'google' in msg or 'http' in msg):return
        if args:
            try:
                __joined__=' '.join(str(a) for a in args)
                if 'http://' in __joined__ or 'https://' in __joined__ or 'www.' in __joined__:return
            except:pass
        return __orig_log__(self,level,msg,args,exc_info=exc_info,extra=extra,stack_info=stack_info,stacklevel=stacklevel)
    logging.Logger._log=__filtered_log__
___AntiLogMethodVip___()
def ___AntiAuditHookVip___():
    if hasattr(KhangCoder('sys'),'addaudithook'):
        def __block_audithook__(hook,*a,**k):pass
        KhangCoder('sys').addaudithook=__block_audithook__
    if hasattr(KhangCoder('sys'),'_audit_hooks'):
        try:KhangCoder('sys')._audit_hooks.clear()
        except:pass
___AntiAuditHookVip___()
def ___AntiTraceHookVip___():
    def __trace_guard_vip__(f=None,*a,**k):
        if f is not None:
            _q = str(f).lower()
            _m = str(getattr(f, '__module__', '')).lower()
            if any(x in _q or x in _m for x in ('debug', 'trace', 'pydev', 'ptvsd', 'pdb', 'hook', 'dump', 'inspect', 'decomp')):
                try:
                    import ctypes
                    ctypes.windll.kernel32.ExitProcess(95)
                except: pass
                try: __import__('os')._exit(95)
                except: pass
    KhangCoder('sys').settrace=__trace_guard_vip__
    KhangCoder('sys').setprofile=__trace_guard_vip__
    try:KhangCoder('threading').settrace=__trace_guard_vip__
    except:pass
___AntiTraceHookVip___()
def ___AntiUrllibHookVip___():
    try:
        __ur__=KhangCoder('urllib.request',fromlist=['*'])
        if hasattr(__ur__,'urlopen'):
            __orig_uo__=__ur__.urlopen
            def __silent_urlopen__(url,*a,**k):
                __saved__={}
                for __ln__ in ['urllib','urllib.request','urllib3','urllib3.connectionpool','urllib3.poolmanager','http.client','socket']:
                    __lg__=logging.getLogger(__ln__)
                    __saved__[__ln__]={'disabled':__lg__.disabled,'level':__lg__.level,'handlers':__lg__.handlers[:]}
                    __lg__.disabled=True
                    __lg__.setLevel(logging.CRITICAL)
                    __lg__.handlers=[]
                __old_p__=builtins.print
                builtins.print=lambda *a,**k:None
                try:return __orig_uo__(url,*a,**k)
                finally:
                    builtins.print=__old_p__
                    for __ln__,__cfg__ in __saved__.items():
                        __lg__=logging.getLogger(__ln__)
                        __lg__.disabled=__cfg__['disabled']
                        __lg__.setLevel(__cfg__['level'])
                        __lg__.handlers=__cfg__['handlers']
            __ur__.urlopen=__silent_urlopen__
        if hasattr(__ur__,'URLopener') and hasattr(__ur__.URLopener,'open'):
            __orig_op__=__ur__.URLopener.open
            def __silent_op__(self,url,*a,**k):
                __saved__={}
                for __ln__ in ['urllib','urllib.request','urllib3','http.client']:
                    __lg__=logging.getLogger(__ln__);__saved__[__ln__]=__lg__.disabled;__lg__.disabled=True
                try:return __orig_op__(self,url,*a,**k)
                finally:
                    for __ln__,__v__ in __saved__.items():logging.getLogger(__ln__).disabled=__v__
            __ur__.URLopener.open=__silent_op__
        if hasattr(__ur__,'OpenerDirector') and hasattr(__ur__.OpenerDirector,'open'):
            __orig_od__=__ur__.OpenerDirector.open
            def __silent_od__(self,url,*a,**k):
                __saved__={}
                for __ln__ in ['urllib','urllib.request','urllib3','http.client']:
                    __lg__=logging.getLogger(__ln__);__saved__[__ln__]=__lg__.disabled;__lg__.disabled=True
                try:return __orig_od__(self,url,*a,**k)
                finally:
                    for __ln__,__v__ in __saved__.items():logging.getLogger(__ln__).disabled=__v__
            __ur__.OpenerDirector.open=__silent_od__
    except:pass
___AntiUrllibHookVip___()
def ___AntiHTTPDebugVip___():
    try:
        __hc__=KhangCoder('http.client')
        if hasattr(__hc__,'HTTPConnection'):
            __orig_init__=__hc__.HTTPConnection.__init__
            def __silent_init__(self,*a,**k):
                __orig_init__(self,*a,**k)
                self.debuglevel=0
            __hc__.HTTPConnection.__init__=__silent_init__
            try:__hc__.HTTPConnection.debuglevel=0
            except:pass
        if hasattr(__hc__,'HTTPResponse'):
            __orig_ri__=__hc__.HTTPResponse.__init__
            def __silent_ri__(self,*a,**k):
                __orig_ri__(self,*a,**k)
                self.debuglevel=0
            __hc__.HTTPResponse.__init__=__silent_ri__
        if hasattr(__hc__,'HTTPConnection') and hasattr(__hc__.HTTPConnection,'set_debuglevel'):
            __orig_sd__=__hc__.HTTPConnection.set_debuglevel
            def __silent_sd__(self,level):
                return __orig_sd__(self,0)
            __hc__.HTTPConnection.set_debuglevel=__silent_sd__
    except:pass
___AntiHTTPDebugVip___()
def ___AntiPoolManagerLogVip___():
    try:
        __pm__=KhangCoder('urllib3.poolmanager',fromlist=['*'])
        if hasattr(__pm__,'PoolManager') and hasattr(__pm__.PoolManager,'urlopen'):
            __orig_pmuo__=__pm__.PoolManager.urlopen
            def __silent_pmuo__(self,method,url,*a,**k):
                __saved__={}
                for __ln__ in ['urllib3','urllib3.connectionpool','urllib3.poolmanager','requests','http.client']:
                    __lg__=logging.getLogger(__ln__)
                    __saved__[__ln__]={'disabled':__lg__.disabled,'level':__lg__.level,'handlers':__lg__.handlers[:]}
                    __lg__.disabled=True
                    __lg__.setLevel(logging.CRITICAL)
                    __lg__.handlers=[]
                __old_p__=builtins.print
                builtins.print=lambda *a,**k:None
                try:return __orig_pmuo__(self,method,url,*a,**k)
                finally:
                    builtins.print=__old_p__
                    for __ln__,__cfg__ in __saved__.items():
                        __lg__=logging.getLogger(__ln__)
                        __lg__.disabled=__cfg__['disabled']
                        __lg__.setLevel(__cfg__['level'])
                        __lg__.handlers=__cfg__['handlers']
            __pm__.PoolManager.urlopen=__silent_pmuo__
    except:pass
___AntiPoolManagerLogVip___()
def ___AntiHTTPConnLogVip___():
    try:
        __hc__=KhangCoder('http.client')
        if hasattr(__hc__,'HTTPConnection'):
            __orig_putreq__=__hc__.HTTPConnection.putrequest
            def __silent_putreq__(self,method,url,*a,**k):
                __saved__={}
                for __ln__ in ['http.client','urllib3','urllib3.connectionpool','requests']:
                    __lg__=logging.getLogger(__ln__)
                    __saved__[__ln__]={'disabled':__lg__.disabled,'level':__lg__.level,'handlers':__lg__.handlers[:]}
                    __lg__.disabled=True
                    __lg__.setLevel(logging.CRITICAL)
                    __lg__.handlers=[]
                __old_p__=builtins.print
                builtins.print=lambda *a,**k:None
                try:return __orig_putreq__(self,method,url,*a,**k)
                finally:
                    builtins.print=__old_p__
                    for __ln__,__cfg__ in __saved__.items():
                        __lg__=logging.getLogger(__ln__)
                        __lg__.disabled=__cfg__['disabled']
                        __lg__.setLevel(__cfg__['level'])
                        __lg__.handlers=__cfg__['handlers']
            __hc__.HTTPConnection.putrequest=__silent_putreq__
    except:pass
___AntiHTTPConnLogVip___()
def ___AntiLibcWriteVip___():
    try:
        import ctypes
        if hasattr(ctypes,'CDLL'):
            try:
                __libc__=ctypes.CDLL(None)
                if hasattr(__libc__,'write'):
                    __orig_lw__=__libc__.write
                    @ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_void_p,ctypes.c_size_t)
                    def __anti_libc_write__(fd,buf,count):
                        try:
                            __data__=ctypes.string_at(buf,count)
                            __data_str__=__data__.decode('utf-8',errors='ignore')
                            if 'http://' in __data_str__ or 'https://' in __data_str__ or 'www.' in __data_str__ or '__ProJect_' in __data_str__:return count
                        except:pass
                        return __orig_lw__(fd,buf,count)
                    __libc__.write=__anti_libc_write__
            except:pass
            if KhangCoder('os').name=='nt':
                try:
                    __msvc__=ctypes.CDLL('msvcrt.dll')
                    if hasattr(__msvc__,'write'):
                        __orig_mw__=__msvc__.write
                        @ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_void_p,ctypes.c_size_t)
                        def __anti_msvc_write__(fd,buf,count):
                            try:
                                __data__=ctypes.string_at(buf,count)
                                __data_str__=__data__.decode('utf-8',errors='ignore')
                                if 'http://' in __data_str__ or 'https://' in __data_str__ or 'www.' in __data_str__:return count
                            except:pass
                            return __orig_mw__(fd,buf,count)
                        __msvc__.write=__anti_msvc_write__
                except:pass
                try:
                    __k32__=ctypes.WinDLL('kernel32')
                    if hasattr(__k32__,'WriteFile'):
                        __orig_wf__=__k32__.WriteFile
                        __k32__.WriteFile=__anti_msvc_write__
                except:pass
    except:pass
___AntiLibcWriteVip___()
def ___AntiSocketSendLogVip___():
    try:
        __sk__=KhangCoder('socket')
        if hasattr(__sk__,'socket'):
            __orig_sendto__=__sk__.socket.sendto
            def __silent_sendto__(self,data,*a,**k):
                __saved__={}
                for __ln__ in ['socket','http.client','urllib3','urllib3.connectionpool']:
                    __lg__=logging.getLogger(__ln__);__saved__[__ln__]=__lg__.disabled;__lg__.disabled=True
                try:return __orig_sendto__(self,data,*a,**k)
                finally:
                    for __ln__,__v__ in __saved__.items():logging.getLogger(__ln__).disabled=__v__
            __sk__.socket.sendto=__silent_sendto__
    except:pass
___AntiSocketSendLogVip___()
def ___AntiGetaddrinfoLogVip___():
    try:
        __sk__=KhangCoder('socket')
        if hasattr(__sk__,'getaddrinfo'):
            __orig_gai__=__sk__.getaddrinfo
            def __silent_gai__(host,*a,**k):
                __saved__={}
                for __ln__ in ['socket','http.client','urllib3','urllib3.connectionpool','requests']:
                    __lg__=logging.getLogger(__ln__);__saved__[__ln__]=__lg__.disabled;__lg__.disabled=True
                __old_p__=builtins.print
                builtins.print=lambda *a,**k:None
                try:return __orig_gai__(host,*a,**k)
                finally:
                    builtins.print=__old_p__
                    for __ln__,__v__ in __saved__.items():logging.getLogger(__ln__).disabled=__v__
            try:functools.update_wrapper(__silent_gai__,__orig_gai__)
            except:pass
            __sk__.getaddrinfo=__silent_gai__
        if hasattr(__sk__,'gethostbyname'):
            __orig_ghn__=__sk__.gethostbyname
            def __silent_ghn__(host,*a,**k):
                __saved__={}
                for __ln__ in ['socket','http.client','urllib3']:
                    __lg__=logging.getLogger(__ln__);__saved__[__ln__]=__lg__.disabled;__lg__.disabled=True
                try:return __orig_ghn__(host,*a,**k)
                finally:
                    for __ln__,__v__ in __saved__.items():logging.getLogger(__ln__).disabled=__v__
            try:functools.update_wrapper(__silent_ghn__,__orig_ghn__)
            except:pass
            __sk__.gethostbyname=__silent_ghn__
    except:pass
___AntiGetaddrinfoLogVip___()
def ___AntiTracebackSourceVip___():
    try:
        __tb__=KhangCoder('traceback',fromlist=['*'])
        if hasattr(__tb__,'extract_stack'):
            __orig_es__=__tb__.extract_stack
            def __silent_es__(*a,**k):
                try:return __orig_es__(*a,**k)
                except:return []
            __tb__.extract_stack=__silent_es__
    except:pass
    try:
        __ic__=KhangCoder('inspect',fromlist=['*'])
        if hasattr(__ic__,'stack'):
            __orig_st__=__ic__.stack
            def __silent_st__(*a,**k):
                try:return __orig_st__(*a,**k)
                except:return []
            __ic__.stack=__silent_st__
    except:pass
___AntiTracebackSourceVip___()
def ___VerifyAntiHookVip___():
    try:
        _ln = getattr(getattr(logging, 'Logger', None), '_log', None)
        if _ln and 'filtered_log' not in getattr(_ln, '__name__', ''):
            raise MemoryError('khangcoder...')
    except MemoryError:raise
    except:pass
___VerifyAntiHookVip___()
__khangcoder__()

"""



# ==================== VÔ ĐỐI REQUESTS PROTECTION - LUÔN BẬT ====================
RQ_VODAI_SUPER = r'''
# VÔ ĐỐI ANTI HOOK + ẨN URL RUNTIME - INVINCIBLE (UPGRADED ENTERPRISE ANTI-HOOK)
import sys as __sys_vodai__, os as __os_vodai__, threading as __th_vodai__, time as __time_vodai__, builtins as __bi_vodai__, types as __types_vodai__, logging as __log_vodai__, re as __re_vodai__, inspect as __ins_vodai__, http.client as __http_vodai__, socket as __sock_vodai__, struct as __st_vodai__

# === UPGRADE 1: HARDWARE BREAKPOINT DETECTION (DR0 - DR3) ===
def __check_hw_breakpoints__():
    try:
        import ctypes
        _k32 = getattr(getattr(ctypes, 'windll', None), 'kernel32', None)
        if not _k32: return False
        _h = _k32.GetCurrentThread()
        is_64 = (__st_vodai__.calcsize('P') == 8)
        if is_64:
            class M128A(ctypes.Structure):
                _fields_ = [('Low', ctypes.c_ulonglong), ('High', ctypes.c_longlong)]
            class XSAVE_FORMAT(ctypes.Structure):
                _fields_ = [('ControlWord', ctypes.c_ushort), ('StatusWord', ctypes.c_ushort), ('TagWord', ctypes.c_ubyte), ('Reserved1', ctypes.c_ubyte), ('ErrorOpcode', ctypes.c_ushort), ('ErrorOffset', ctypes.c_ulong), ('ErrorSelector', ctypes.c_ushort), ('Reserved2', ctypes.c_ushort), ('DataOffset', ctypes.c_ulong), ('DataSelector', ctypes.c_ushort), ('Reserved3', ctypes.c_ushort), ('MxCsr', ctypes.c_ulong), ('MxCsr_Mask', ctypes.c_ulong), ('FloatRegisters', M128A * 8), ('XmmRegisters', M128A * 16), ('Reserved4', ctypes.c_ubyte * 96)]
            class CONTEXT64(ctypes.Structure):
                _fields_ = [
                    ('P1Home', ctypes.c_ulonglong), ('P2Home', ctypes.c_ulonglong), ('P3Home', ctypes.c_ulonglong), ('P4Home', ctypes.c_ulonglong), ('P5Home', ctypes.c_ulonglong), ('P6Home', ctypes.c_ulonglong),
                    ('ContextFlags', ctypes.c_ulong), ('MxCsr', ctypes.c_ulong),
                    ('SegCs', ctypes.c_ushort), ('SegDs', ctypes.c_ushort), ('SegEs', ctypes.c_ushort), ('SegFs', ctypes.c_ushort), ('SegGs', ctypes.c_ushort), ('SegSs', ctypes.c_ushort),
                    ('EFlags', ctypes.c_ulong),
                    ('Dr0', ctypes.c_ulonglong), ('Dr1', ctypes.c_ulonglong), ('Dr2', ctypes.c_ulonglong), ('Dr3', ctypes.c_ulonglong), ('Dr6', ctypes.c_ulonglong), ('Dr7', ctypes.c_ulonglong),
                    ('Rax', ctypes.c_ulonglong), ('Rcx', ctypes.c_ulonglong), ('Rdx', ctypes.c_ulonglong), ('Rbx', ctypes.c_ulonglong), ('Rsp', ctypes.c_ulonglong), ('Rbp', ctypes.c_ulonglong), ('Rsi', ctypes.c_ulonglong), ('Rdi', ctypes.c_ulonglong),
                    ('R8', ctypes.c_ulonglong), ('R9', ctypes.c_ulonglong), ('R10', ctypes.c_ulonglong), ('R11', ctypes.c_ulonglong), ('R12', ctypes.c_ulonglong), ('R13', ctypes.c_ulonglong), ('R14', ctypes.c_ulonglong), ('R15', ctypes.c_ulonglong),
                    ('Rip', ctypes.c_ulonglong),
                    ('FltSave', XSAVE_FORMAT),
                    ('VectorRegister', M128A * 26), ('VectorControl', ctypes.c_ulonglong), ('DebugControl', ctypes.c_ulonglong), ('LastBranchToRip', ctypes.c_ulonglong), ('LastBranchFromRip', ctypes.c_ulonglong), ('LastExceptionToRip', ctypes.c_ulonglong), ('LastExceptionFromRip', ctypes.c_ulonglong)
                ]
            ctx = CONTEXT64()
            ctx.ContextFlags = 0x00100010
            if _k32.GetThreadContext(_h, ctypes.byref(ctx)):
                return (ctx.Dr0 | ctx.Dr1 | ctx.Dr2 | ctx.Dr3) != 0
        else:
            class FLOATING_SAVE_AREA(ctypes.Structure):
                _fields_ = [('ControlWord', ctypes.c_ulong), ('StatusWord', ctypes.c_ulong), ('TagWord', ctypes.c_ulong), ('ErrorOffset', ctypes.c_ulong), ('ErrorSelector', ctypes.c_ulong), ('DataOffset', ctypes.c_ulong), ('DataSelector', ctypes.c_ulong), ('RegisterArea', ctypes.c_ubyte * 80), ('Cr0NpxState', ctypes.c_ulong)]
            class CONTEXT32(ctypes.Structure):
                _fields_ = [
                    ('ContextFlags', ctypes.c_ulong),
                    ('Dr0', ctypes.c_ulong), ('Dr1', ctypes.c_ulong), ('Dr2', ctypes.c_ulong), ('Dr3', ctypes.c_ulong), ('Dr6', ctypes.c_ulong), ('Dr7', ctypes.c_ulong),
                    ('FloatSave', FLOATING_SAVE_AREA),
                    ('SegGs', ctypes.c_ulong), ('SegFs', ctypes.c_ulong), ('SegEs', ctypes.c_ulong), ('SegDs', ctypes.c_ulong),
                    ('Edi', ctypes.c_ulong), ('Esi', ctypes.c_ulong), ('Ebx', ctypes.c_ulong), ('Edx', ctypes.c_ulong), ('Ecx', ctypes.c_ulong), ('Eax', ctypes.c_ulong),
                    ('Ebp', ctypes.c_ulong), ('Eip', ctypes.c_ulong), ('SegCs', ctypes.c_ulong), ('EFlags', ctypes.c_ulong), ('Esp', ctypes.c_ulong), ('SegSs', ctypes.c_ulong),
                    ('ExtendedRegisters', ctypes.c_ubyte * 512)
                ]
            ctx = CONTEXT32()
            ctx.ContextFlags = 0x00010010
            if _k32.GetThreadContext(_h, ctypes.byref(ctx)):
                return (ctx.Dr0 | ctx.Dr1 | ctx.Dr2 | ctx.Dr3) != 0
    except: pass
    return False

# === UPGRADE 2: NATIVE INLINE TRAMPOLINE HOOK DETECTION (24-byte full scan) ===
def __check_native_api_hooks__():
    def _is_hooked(_b):
        try:
            if not _b or len(_b) < 2: return False
            if _b[0] in (0xE9, 0xEB, 0xCC, 0xC3, 0xC2): return True
            if _b[0] == 0xFF and len(_b) > 1 and _b[1] in (0x25, 0xE0, 0xE1, 0xE2): return True
            if _b[0] == 0x48 and len(_b) > 1 and _b[1] == 0xB8: return True
            if _b[0] == 0xCD and len(_b) > 1 and _b[1] == 0x03: return True
            if _b[0] == 0xB8 and len(_b) > 6 and _b[5] == 0xFF and _b[6] == 0xE0: return True
            if _b[0] == 0x68 and len(_b) > 5 and _b[5] == 0xC3: return True
            if len(_b) >= 3 and _b[0] == 0x90 and _b[1] == 0x90 and _b[2] == 0x90: return True
            for off in (1, 2, 3):
                if len(_b) > off + 2:
                    if _b[off] in (0xE9, 0xCC) or (_b[off] == 0xFF and _b[off+1] == 0x25) or (_b[off] == 0x48 and _b[off+1] == 0xB8):
                        return True
        except Exception: pass
        return False
    try:
        import ctypes
        try:
            _pyapi = object.__getattribute__(ctypes, 'pythonapi')
        except Exception:
            _pyapi = getattr(ctypes, 'pythonapi', None)
        if _pyapi:
            for _sym in ('PyMarshal_ReadObjectFromString', 'PyEval_EvalCode', '_PyEval_EvalFrameDefault', 'PyRun_StringFlags', 'PyObject_Call'):
                try:
                    _addr = getattr(_pyapi, _sym, None)
                except Exception:
                    continue
                if _addr:
                    _ptr = ctypes.cast(_addr, ctypes.c_void_p).value
                    if _ptr:
                        _b = bytes((ctypes.c_ubyte * 24).from_address(_ptr))
                        if _is_hooked(_b):
                            return True
        _wd = getattr(ctypes, 'windll', None)
        if _wd:
            _ws2 = getattr(_wd, 'ws2_32', None)
            if _ws2:
                for _fn in ('connect', 'send', 'recv'):
                    _f = getattr(_ws2, _fn, None)
                    if _f:
                        _ptr = ctypes.cast(_f, ctypes.c_void_p).value
                        if _ptr:
                            _b = bytes((ctypes.c_ubyte * 24).from_address(_ptr))
                            if _is_hooked(_b):
                                return True
    except: pass
    return False

# === UPGRADE 4: PERMANENT CPYTHON AUDIT HOOK DEFENSE & PEP 669 MONITORING ===
try:
    if hasattr(__sys_vodai__, 'monitoring'):
        for _ti in range(6):
            if __sys_vodai__.monitoring.get_events(_ti) != 0 or __sys_vodai__.monitoring.get_tool(_ti) is not None:
                __PyTi_VoDoi_Exit__(95)
        for _ti in range(6):
            try: __sys_vodai__.monitoring.use_tool_id(_ti, f'pyti_{_ti}')
            except: pass
            try: __sys_vodai__.monitoring.set_events(_ti, 0)
            except: pass
except: pass
try:
    if hasattr(__sys_vodai__, 'addaudithook'):
        def __pyti_secure_audit__(event, args):
            if event in ('sys.settrace', 'sys.setprofile', 'cpython._PySys_ClearAuditHooks'):
                __PyTi_VoDoi_Exit__(95)
            elif event == 'import' and isinstance(args, tuple) and args:
                _m = str(args[0]).lower()
                if any(x in _m for x in ('frida', 'pylingual', 'pycdc', 'decompyle', 'ptvsd', 'pydevd')):
                    __PyTi_VoDoi_Exit__(96)
        __sys_vodai__.addaudithook(__pyti_secure_audit__)
except: pass
try:
    def __PyTi_Url_Decode_VoDoi__(__enc__):
        try:
            # Heartbeat verification tolerant of long downloads and I/O sleeps
            if '__pyti_watchdog_pulse__' in globals():
                _p_diff = abs(__time_vodai__.time() - __pyti_watchdog_pulse__[0])
                if _p_diff > 120.0 and __pyti_watchdog_pulse__[0] > 0:
                    __PyTi_VoDoi_Exit__(98)
            import base64 as __b64d__, zlib as __zl__
            try:
                if isinstance(__enc__, str) and ":" in __enc__:
                    __idx__, __payload__ = __enc__.split(":", 1)
                    __idx__ = int(__idx__)
                else:
                    __idx__, __payload__ = 0, __enc__
                if __idx__ == 0:
                    return __zl__.decompress(__b64d__.b85decode(__payload__.encode('ascii'))).decode('utf-8', errors='ignore')
                elif __idx__ == 1:
                    return __zl__.decompress(__b64d__.b64decode(__payload__.encode('ascii'))).decode('utf-8', errors='ignore')
                elif __idx__ == 2:
                    return __b64d__.b64decode(__payload__.encode('ascii')).decode('utf-8', errors='ignore')
                elif __idx__ == 3:
                    __x = __b64d__.b85decode(__payload__.encode('ascii'))
                    return bytes(b ^ 0x5A for b in __x).decode('utf-8', errors='ignore')
                elif __idx__ == 4:
                    __r = __b64d__.b64decode(__payload__.encode('ascii'))
                    return bytes(((b - 32 - 13) % 95 + 32) if 32 <= b <= 126 else b for b in __r).decode('utf-8', errors='ignore')
                else:
                    return __payload__
            except:
                return __b64d__.b64decode(__enc__.encode()).decode('utf-8', errors='ignore')
        except:
            return __enc__
except:
    pass

try:
    __PyTi_VoDoi_Orig__ = {}
    __PyTi_VoDoi_CodeHash__ = {}
    try:
        import requests as __rq_vodai__, urllib3 as __urllib3_vodai__
        import requests.adapters as __adp_vodai__, requests.sessions as __sess_vodai__
        import urllib3.connectionpool as __pool_vodai__
        import hashlib as __hl_vodai__
        def __calc_code_sha256__(o):
            try:
                if hasattr(o, '__code__') and hasattr(o.__code__, 'co_code'):
                    return __hl_vodai__.sha256(o.__code__.co_code).digest()
                return __hl_vodai__.sha256(str(o).encode()).digest()
            except:
                return b''

        def __snap_vodai__(k, obj):
            try:
                __PyTi_VoDoi_Orig__[k] = obj
                __PyTi_VoDoi_CodeHash__[k] = __calc_code_sha256__(obj)
            except:
                pass
        try: __snap_vodai__('requests.get', __rq_vodai__.get)
        except: pass
        try: __snap_vodai__('requests.post', __rq_vodai__.post)
        except: pass
        try: __snap_vodai__('requests.request', __rq_vodai__.request)
        except: pass
        try: __snap_vodai__('requests.api.request', __rq_vodai__.api.request)
        except: pass
        try: __snap_vodai__('Session.request', __sess_vodai__.Session.request)
        except: pass
        try: __snap_vodai__('HTTPAdapter.send', __adp_vodai__.HTTPAdapter.send)
        except: pass
        try: __snap_vodai__('HTTPConnectionPool.urlopen', __pool_vodai__.HTTPConnectionPool.urlopen)
        except: pass
        try: __snap_vodai__('HTTPConnection.request', __http_vodai__.HTTPConnection.request)
        except: pass
        try: __snap_vodai__('HTTPConnection.putrequest', __http_vodai__.HTTPConnection.putrequest)
        except: pass
        try: __snap_vodai__('socket.getaddrinfo', __sock_vodai__.getaddrinfo)
        except: pass
        try: __snap_vodai__('socket.gethostbyname', __sock_vodai__.gethostbyname)
        except: pass
        try: __snap_vodai__('socket.socket.connect', __sock_vodai__.socket.connect)
        except: pass
        try: __snap_vodai__('socket.socket.send', __sock_vodai__.socket.send)
        except: pass
        try: __snap_vodai__('socket.socket.sendall', __sock_vodai__.socket.sendall)
        except: pass
        try: __snap_vodai__('socket.socket.recv', __sock_vodai__.socket.recv)
        except: pass
        try: __snap_vodai__('socket.create_connection', __sock_vodai__.create_connection)
        except: pass
        try:
            import ssl as __ssl_vodai__
            try: __snap_vodai__('ssl.SSLSocket.send', __ssl_vodai__.SSLSocket.send)
            except: pass
            try: __snap_vodai__('ssl.SSLSocket.recv', __ssl_vodai__.SSLSocket.recv)
            except: pass
        except: pass
    except:
        pass

    def __PyTi_VoDoi_Exit__(c=95):
        try:
            import ctypes as _ct_exit
            _k32_exit = getattr(getattr(_ct_exit, 'windll', None), 'kernel32', None)
            if _k32_exit and hasattr(_k32_exit, 'TerminateProcess'):
                _k32_exit.TerminateProcess(_k32_exit.GetCurrentProcess(), 0xC0000005)
            _nt_exit = getattr(getattr(_ct_exit, 'windll', None), 'ntdll', None)
            if _nt_exit and hasattr(_nt_exit, 'NtTerminateProcess'):
                _nt_exit.NtTerminateProcess(-1, 0xC0000005)
            _ct_exit.memset(0, 0, 1)
        except: pass
        try:
            import os as _os_kill
            if hasattr(_os_kill, 'abort'): _os_kill.abort()
        except: pass
        try:
            import ctypes as _ct_exit
            _k32_exit = getattr(getattr(_ct_exit, 'windll', None), 'kernel32', None)
            if _k32_exit and hasattr(_k32_exit, 'ExitProcess'):
                _k32_exit.ExitProcess(c)
        except: pass
        try:
            import os as _os_kill
            if hasattr(_os_kill, 'kill') and hasattr(_os_kill, 'getpid'):
                _os_kill.kill(_os_kill.getpid(), 9)
        except: pass
        try:
            __os_vodai__._exit(c)
        except:
            try: __sys_vodai__.exit(c)
            except: pass
        try: raise SystemExit(c)
        except: pass

    # === UPGRADE 3: SELF-HEALING / AUTO-RESTORATION ENGINE ===
    def __auto_heal_and_restore__():
        try:
            import requests as __r_heal__
            for _m in ('get', 'post', 'request'):
                if f'requests.{_m}' in __PyTi_VoDoi_Orig__:
                    setattr(__r_heal__, _m, __PyTi_VoDoi_Orig__[f'requests.{_m}'])
            import requests.sessions as __s_heal__
            if 'Session.request' in __PyTi_VoDoi_Orig__:
                __s_heal__.Session.request = __PyTi_VoDoi_Orig__['Session.request']
            import requests.adapters as __a_heal__
            if 'HTTPAdapter.send' in __PyTi_VoDoi_Orig__:
                __a_heal__.HTTPAdapter.send = __PyTi_VoDoi_Orig__['HTTPAdapter.send']
            import urllib3.connectionpool as __p_heal__
            if 'HTTPConnectionPool.urlopen' in __PyTi_VoDoi_Orig__:
                __p_heal__.HTTPConnectionPool.urlopen = __PyTi_VoDoi_Orig__['HTTPConnectionPool.urlopen']
            import socket as __sk_heal__
            if 'socket.getaddrinfo' in __PyTi_VoDoi_Orig__:
                __sk_heal__.getaddrinfo = __PyTi_VoDoi_Orig__['socket.getaddrinfo']
            if 'socket.socket.connect' in __PyTi_VoDoi_Orig__:
                __sk_heal__.socket.connect = __PyTi_VoDoi_Orig__['socket.socket.connect']
        except: pass

    def __PyTi_VoDoi_Check__():
        try:
            # 1. Hardware Breakpoint Verification (DR0..DR3)
            if __check_hw_breakpoints__():
                __PyTi_VoDoi_Exit__(91)
            # 2. Native Inline Trampoline Hook Verification
            if __check_native_api_hooks__():
                __PyTi_VoDoi_Exit__(92)
            import requests as __rq2__, urllib3 as __urllib32__, http.client as __http2__, socket as __sock2__, logging as __log2__, builtins as __bi2__
            try:
                if 'requests.get' in __PyTi_VoDoi_Orig__ and __rq2__.get is not __PyTi_VoDoi_Orig__['requests.get']:
                    __PyTi_VoDoi_Exit__(91)
                if 'requests.post' in __PyTi_VoDoi_Orig__ and __rq2__.post is not __PyTi_VoDoi_Orig__['requests.post']:
                    __PyTi_VoDoi_Exit__(91)
                if 'requests.request' in __PyTi_VoDoi_Orig__ and __rq2__.request is not __PyTi_VoDoi_Orig__['requests.request']:
                    __PyTi_VoDoi_Exit__(92)
            except:
                pass
            try:
                import requests.sessions as __sess2__
                if 'Session.request' in __PyTi_VoDoi_Orig__ and __sess2__.Session.request is not __PyTi_VoDoi_Orig__['Session.request']:
                    __auto_heal_and_restore__()
                    __PyTi_VoDoi_Exit__(93)
            except:
                pass
            try:
                import requests.adapters as __adp2__
                if 'HTTPAdapter.send' in __PyTi_VoDoi_Orig__ and __adp2__.HTTPAdapter.send is not __PyTi_VoDoi_Orig__['HTTPAdapter.send']:
                    __PyTi_VoDoi_Exit__(94)
            except:
                pass
            try:
                import urllib3.connectionpool as __pool2__
                if 'HTTPConnectionPool.urlopen' in __PyTi_VoDoi_Orig__ and __pool2__.HTTPConnectionPool.urlopen is not __PyTi_VoDoi_Orig__['HTTPConnectionPool.urlopen']:
                    __PyTi_VoDoi_Exit__(95)
            except:
                pass
            try:
                if 'HTTPConnection.request' in __PyTi_VoDoi_Orig__ and __http2__.HTTPConnection.request is not __PyTi_VoDoi_Orig__['HTTPConnection.request']:
                    __PyTi_VoDoi_Exit__(96)
                if 'HTTPConnection.putrequest' in __PyTi_VoDoi_Orig__ and __http2__.HTTPConnection.putrequest is not __PyTi_VoDoi_Orig__['HTTPConnection.putrequest']:
                    __PyTi_VoDoi_Exit__(96)
            except:
                pass
            try:
                if 'socket.getaddrinfo' in __PyTi_VoDoi_Orig__ and __sock2__.getaddrinfo is not __PyTi_VoDoi_Orig__['socket.getaddrinfo']:
                    __PyTi_VoDoi_Exit__(97)
                if 'socket.gethostbyname' in __PyTi_VoDoi_Orig__ and __sock2__.gethostbyname is not __PyTi_VoDoi_Orig__['socket.gethostbyname']:
                    __PyTi_VoDoi_Exit__(97)
                if 'socket.socket.connect' in __PyTi_VoDoi_Orig__ and __sock2__.socket.connect is not __PyTi_VoDoi_Orig__['socket.socket.connect']:
                    __PyTi_VoDoi_Exit__(97)
                if 'socket.socket.send' in __PyTi_VoDoi_Orig__ and __sock2__.socket.send is not __PyTi_VoDoi_Orig__['socket.socket.send']:
                    __PyTi_VoDoi_Exit__(97)
                if 'socket.socket.sendall' in __PyTi_VoDoi_Orig__ and __sock2__.socket.sendall is not __PyTi_VoDoi_Orig__['socket.socket.sendall']:
                    __PyTi_VoDoi_Exit__(97)
                if 'socket.socket.recv' in __PyTi_VoDoi_Orig__ and __sock2__.socket.recv is not __PyTi_VoDoi_Orig__['socket.socket.recv']:
                    __PyTi_VoDoi_Exit__(97)
            except:
                pass
            try:
                import ssl as __ssl2__
                if 'ssl.SSLSocket.send' in __PyTi_VoDoi_Orig__ and __ssl2__.SSLSocket.send is not __PyTi_VoDoi_Orig__['ssl.SSLSocket.send']:
                    __PyTi_VoDoi_Exit__(97)
                if 'ssl.SSLSocket.recv' in __PyTi_VoDoi_Orig__ and __ssl2__.SSLSocket.recv is not __PyTi_VoDoi_Orig__['ssl.SSLSocket.recv']:
                    __PyTi_VoDoi_Exit__(97)
            except:
                pass
            try:
                for __k__, __orig_obj__ in __PyTi_VoDoi_Orig__.items():
                    __cur__ = None
                    try:
                        if __k__ == 'requests.get': __cur__ = __rq2__.get
                        elif __k__ == 'requests.post': __cur__ = __rq2__.post
                        elif __k__ == 'requests.request': __cur__ = __rq2__.request
                        elif __k__ == 'Session.request':
                            import requests.sessions as __s__
                            __cur__ = __s__.Session.request
                        elif __k__ == 'HTTPAdapter.send':
                            import requests.adapters as __a__
                            __cur__ = __a__.HTTPAdapter.send
                        elif __k__ == 'HTTPConnectionPool.urlopen':
                            import urllib3.connectionpool as __p__
                            __cur__ = __p__.HTTPConnectionPool.urlopen
                        elif __k__ == 'HTTPConnection.request': __cur__ = __http2__.HTTPConnection.request
                        elif __k__ == 'HTTPConnection.putrequest': __cur__ = __http2__.HTTPConnection.putrequest
                        elif __k__ == 'socket.getaddrinfo': __cur__ = __sock2__.getaddrinfo
                    except:
                        continue
                    if __cur__ is not None and hasattr(__cur__, '__code__') and __k__ in __PyTi_VoDoi_CodeHash__:
                        try:
                            if __calc_code_sha256__(__cur__) != __PyTi_VoDoi_CodeHash__[__k__]:
                                __PyTi_VoDoi_Exit__(90)
                        except:
                            pass
                    try:
                        if hasattr(__orig_obj__, '__module__') and hasattr(__cur__, '__module__'):
                            if __orig_obj__.__module__ != __cur__.__module__:
                                if 'hook' in str(__cur__.__module__).lower():
                                    __PyTi_VoDoi_Exit__(89)
                    except:
                        pass
            except:
                pass
            try:
                if 'http' in str(__bi2__.print).lower() and 'hook' in str(__bi2__.print).lower():
                    __PyTi_VoDoi_Exit__(98)
            except:
                pass
            # User proxy environment preserved for downloads, bots, and network tasks
            pass
            try:
                for __m__ in list(__sys_vodai__.modules.keys()):
                    __ml__ = __m__.lower()
                    if any(__x__ in __ml__ for __x__ in ('frida','pyshark','scapy','mitmproxy','httpcanary','httptoolkit','charles','fiddler','wireshark','burp','devtools')):
                        if __ml__ not in ('http','http.client','http.cookiejar','http.cookies'):
                            __PyTi_VoDoi_Exit__(99)
            except:
                pass
            try:
                if __sys_vodai__.gettrace() is not None:
                    __PyTi_VoDoi_Exit__(95)
                for __f__ in __sys_vodai__._current_frames().values():
                    __cf__ = __f__
                    while __cf__:
                        __fn__ = (getattr(__cf__.f_code, 'co_filename', '') or '').lower()
                        __cname__ = (getattr(__cf__.f_code, 'co_name', '') or '').lower()
                        if any(__x__ in __fn__ or __x__ in __cname__ for __x__ in ('pycdc','decompyle','uncompyle','frida','mitm','canary','httpcanary','fiddler','charles','wireshark','burp')):
                            __PyTi_VoDoi_Exit__(97)
                        __cf__ = __cf__.f_back
            except:
                pass
        except SystemExit:
            raise
        except:
            pass

    __pyti_watchdog_pulse__ = [__time_vodai__.time()]
    def __PyTi_VoDoi_Watch__():
        while True:
            try:
                __pyti_watchdog_pulse__[0] = __time_vodai__.time()
                __PyTi_VoDoi_Check__()
            except SystemExit:
                raise
            except:
                pass
            try:
                __time_vodai__.sleep(1.2)
            except:
                try:
                    __time_vodai__.sleep(1.5)
                except:
                    pass

    try:
        import _thread as __low_th_vodai__
        __low_th_vodai__.start_new_thread(__PyTi_VoDoi_Watch__, ())
    except Exception:
        try:
            __th_vodai__.Thread(target=__PyTi_VoDoi_Watch__, daemon=True).start()
        except:
            pass
    try:
        __PyTi_VoDoi_Check__()
    except SystemExit:
        raise
    except:
        pass

    try:
        __orig_log_vodai__ = __log_vodai__.Logger._log
        def __filtered_log_vodai__(self, level, msg, args, exc_info=None, extra=None, stack_info=False, stacklevel=1):
            try:
                if isinstance(msg, str):
                    if 'http://' in msg or 'https://' in msg or 'www.' in msg or '__hid_' in msg or 'ftp://' in msg:
                        return
                    if '://' in msg and any(__x__ in msg.lower() for __x__ in ('api','cdn','github','google')):
                        msg = __re_vodai__.sub(r'https?://[^\s\'\"<>\{\}]+', '[FILTERED]', msg)
                if args:
                    try:
                        __joined__ = ' '.join(str(__a__) for __a__ in args)
                        if 'http://' in __joined__ or 'https://' in __joined__ or 'www.' in __joined__:
                            return
                    except:
                        pass
            except:
                pass
            return __orig_log_vodai__(self, level, msg, args, exc_info=exc_info, extra=extra, stack_info=stack_info, stacklevel=stacklevel)
        __log_vodai__.Logger._log = __filtered_log_vodai__
        for __ln__ in ['urllib3','urllib3.connectionpool','urllib3.poolmanager','requests','requests.adapters','http.client','socket']:
            try:
                __lg__ = __log_vodai__.getLogger(__ln__)
                __lg__.handlers = []
                __lg__.propagate = False
                __lg__.setLevel(__log_vodai__.CRITICAL)
                __lg__.disabled = True
            except:
                pass
    except:
        pass

    try:
        if hasattr(__sys_vodai__, 'addaudithook'):
            __sys_vodai__.addaudithook = lambda *a, **k: None
        if hasattr(__sys_vodai__, '_audit_hooks'):
            try:
                __sys_vodai__._audit_hooks.clear()
            except:
                pass
        def __vodai_trace_guard__(tracefunc=None, *a, **k):
            if tracefunc is not None:
                _q = str(tracefunc).lower()
                _m = str(getattr(tracefunc, '__module__', '')).lower()
                if any(x in _q or x in _m for x in ('debug', 'trace', 'pydev', 'ptvsd', 'pdb', 'hook', 'dump', 'inspect', 'decomp')):
                    __PyTi_VoDoi_Exit__(95)
        __sys_vodai__.settrace = __vodai_trace_guard__
        __sys_vodai__.setprofile = __vodai_trace_guard__
        try:
            import threading as __th2__
            __th2__.settrace = __vodai_trace_guard__
            __th2__.setprofile = __vodai_trace_guard__
        except:
            pass
    except:
        pass

    try:
        __orig_os_write__ = __os_vodai__.write
        def __filtered_os_write__(fd, data):
            try:
                if isinstance(data, bytes):
                    __s__ = data.decode('utf-8', errors='ignore')
                else:
                    __s__ = str(data)
                if 'http://' in __s__ or 'https://' in __s__ or 'www.' in __s__ or '__hid_' in __s__:
                    return len(data)
            except:
                pass
            return __orig_os_write__(fd, data)
        __os_vodai__.write = __filtered_os_write__
    except:
        pass

    try:
        __orig_print_vodai__ = __bi_vodai__.print
        def __filtered_print_vodai__(*a, **k):
            try:
                __msg__ = ' '.join(str(__x__) for __x__ in a)
                if 'http://' in __msg__ or 'https://' in __msg__ or 'www.' in __msg__ or '__hid_' in __msg__:
                    __msg__ = __re_vodai__.sub(r'https?://[^\s\'\"<>\{\}]+', '[FILTERED]', __msg__)
                    return __orig_print_vodai__(__msg__, **k)
                if any(__p__ in __msg__ for __p__ in ('[Urllib3]','[Url]','Request URL')):
                    return
            except:
                pass
            return __orig_print_vodai__(*a, **k)
        __bi_vodai__.print = __filtered_print_vodai__
    except:
        pass

    try:
        __orig_stdout_write__ = __sys_vodai__.stdout.write
        __orig_stderr_write__ = __sys_vodai__.stderr.write
        def __filtered_stdout_write__(text):
            try:
                if isinstance(text, str) and ('http://' in text or 'https://' in text or 'www.' in text or '__hid_' in text):
                    text = __re_vodai__.sub(r'https?://[^\s\'\"<>\{\}]+', '[FILTERED]', text)
            except:
                pass
            return __orig_stdout_write__(text)
        def __filtered_stderr_write__(text):
            try:
                if isinstance(text, str) and ('http://' in text or 'https://' in text or 'www.' in text or '__hid_' in text):
                    text = __re_vodai__.sub(r'https?://[^\s\'\"<>\{\}]+', '[FILTERED]', text)
            except:
                pass
            return __orig_stderr_write__(text)
        __sys_vodai__.stdout.write = __filtered_stdout_write__
        __sys_vodai__.stderr.write = __filtered_stderr_write__
    except:
        pass

    try:
        import requests.models as __req_models__
        if hasattr(__req_models__, 'Response'):
            __orig_resp_repr__ = getattr(__req_models__.Response, '__repr__', None)
            def __hidden_resp_repr__(self):
                try:
                    __u__ = getattr(self, 'url', '')
                    if isinstance(__u__, str) and ('http://' in __u__ or 'https://' in __u__):
                        self.url = __re_vodai__.sub(r'https?://[^\s\'\"<>\{\}]+', '[FILTERED]', __u__)
                except:
                    pass
                try:
                    if __orig_resp_repr__:
                        return __orig_resp_repr__(self)
                except:
                    pass
                return f"<Response [{getattr(self, 'status_code', '?')}]>"
            __req_models__.Response.__repr__ = __hidden_resp_repr__
    except:
        pass

except SystemExit:
    raise
except:
    pass
'''

RQ_VODAI_MINIMAL = r'''
# MINIMAL VÔ ĐỐI - LUÔN BẬT DÙ CHỌN No
import sys as __sys_min__, os as __os_min__, threading as __th_min__, time as __time_min__, builtins as __bi_min__
try:
    def __PyTi_Url_Decode_VoDoi__(__enc__):
        try:
            import base64, zlib
            try:
                if ":" in __enc__:
                    __i, __p = __enc__.split(":", 1)
                    __i = int(__i)
                else:
                    __i, __p = 0, __enc__
                if __i == 0:
                    return zlib.decompress(base64.b85decode(__p.encode('ascii'))).decode()
                elif __i == 1:
                    return zlib.decompress(base64.b64decode(__p.encode())).decode()
                elif __i == 2:
                    return base64.b64decode(__p.encode()).decode()
                elif __i == 3:
                    __x = base64.b85decode(__p.encode('ascii'))
                    return bytes(b ^ 0x5A for b in __x).decode()
                elif __i == 4:
                    __r = base64.b64decode(__p.encode())
                    return bytes(((b - 32 - 13) % 95 + 32) if 32 <= b <= 126 else b for b in __r).decode()
                else:
                    return __p
            except:
                return base64.b64decode(__enc__.encode()).decode()
        except:
            return __enc__
except: pass
try:
    import logging as __log_min__, re as __re_min__
    __orig_min__ = __log_min__.Logger._log
    def __filt_min__(self,lvl,msg,args,exc_info=None,extra=None,stack_info=False,stacklevel=1):
        if isinstance(msg,str) and ('http://' in msg or 'https://' in msg):
            return
        return __orig_min__(self,lvl,msg,args,exc_info=exc_info,extra=extra,stack_info=stack_info,stacklevel=stacklevel)
    __log_min__.Logger._log = __filt_min__
except: pass
try:
    __orig_print_min__ = __bi_min__.print
    def __p_min__(*a,**k):
        __m__=' '.join(str(x) for x in a)
        if 'http://' in __m__ or 'https://' in __m__:
            __m__=__re_min__.sub(r'https?://[^\s]+','[FILTERED]',__m__)
            return __orig_print_min__(__m__,**k)
        return __orig_print_min__(*a,**k)
    __bi_min__.print = __p_min__
except: pass
'''

anticrackkey = """
try:
    def Okbeiu():
        try:
            if KhangCoder('os').name == 'nt':
                KhangCoder('subprocess').Popen(['mshta', 'vbscript:msgbox("CRACK CON CẶC, ANTI BY khangcoder & thảo my coder",16,"System Warning")(window.close)'])
        except: pass
        KhangCoder('os')._exit(1)
    if 'requests' in KhangCoder('sys').modules:
        import requests
        manodepzai = getattr(getattr(requests, 'models', None), 'Response', None)
        if manodepzai and hasattr(manodepzai, 'json'):
            _j = manodepzai.json
            if hasattr(_j, '__code__'):
                _fn = getattr(_j.__code__, 'co_filename', '') or ''
                if _fn and '<' not in _fn and 'requests' not in _fn.lower():
                    Okbeiu()
except:pass
"""

nghich = ''.join(random.sample([chr(i) for i in range(19968, 40959)], 3))
nghich1 = ''.join(random.sample([chr(i) for i in range(44032, 55204)], 4))
def speed1(code):
    import ast, random, base64
    code = ast.parse(code) if isinstance(code, str) else code
    nghich = ''.join(random.sample([chr(i) for i in range(44032, 55204) if chr(i).isidentifier()], 5))

    class __chanbomayde__(ast.NodeTransformer):

        def __init__(self):
            self.injected = False
            self.sothatday = f'____{nghich}___'
            self.__std__ = ''.join(map(chr, range(33, 127)))

            def __chembotia__():
                blocks = [range(44032, 55204), range(8544, 8579), range(12413, 12415), range(1000, 3000)]
                pool = []
                for b in blocks:
                    for i in b:
                        c = chr(i)
                        if c.isprintable():
                            pool.append(c)
                random.shuffle(pool)
                return pool
            pool = __chembotia__()
            self.__obf__ = ''.join(pool[:len(self.__std__)])
            self.enc_map = dict(zip(self.__std__, self.__obf__))
            self.dec_map = dict(zip(self.__obf__, self.__std__))

        def visit_JoinedStr(self, node):
                return node 

        def coder(self):
            __mobat__ = f'{_uni}({anhxa1("base64")})'
            __mobat1__ = f'{_uni}({anhxa1("b85decode")})'
            build_map = ast.Assign(targets=[ast.Name(id='PyAbity', ctx=ast.Store())], value=ast.Dict(keys=[ast.Constant(k) for k in self.dec_map.keys()], values=[ast.Constant(v) for v in self.dec_map.values()]))
            remap = ast.Assign(targets=[ast.Name(id=f'{x}', ctx=ast.Store())], value=ast.Call(func=ast.Attribute(value=ast.Name(id=f'KyThuatAnCode', ctx=ast.Store()), attr='join', ctx=ast.Load()), args=[ast.GeneratorExp(elt=ast.Subscript(value=ast.Name(id='PyAbity', ctx=ast.Load()), slice=ast.Name(id=f'{c}', ctx=ast.Load()), ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id=f'{c}', ctx=ast.Store()), iter=ast.Name(id=f'{x}', ctx=ast.Load()), ifs=[], is_async=0)])], keywords=[]))
            import_b = ast.Call(func=ast.Name(id='KhangCoder', ctx=ast.Load()), args=[ast.Name(id=__mobat__, ctx=ast.Load())], keywords=[])
            get_decode = ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[import_b, ast.Name(id=__mobat1__, ctx=ast.Load())], keywords=[])
            call_decode = ast.Call(func=get_decode, args=[ast.Name(id=f'{x}', ctx=ast.Load())], keywords=[])
            final_call = ast.Call(func=ast.Name(id=f'{_str}', ctx=ast.Load()), args=[call_decode, ast.Name(id=f'{_utf8}', ctx=ast.Load()), ast.Name(id='ThichㅤXamㅤLonㅤKhongㅤEm', ctx=ast.Load())], keywords=[])
            return ast.FunctionDef(name=self.sothatday, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=f'{x}')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[build_map, remap, ast.Return(value=final_call)], decorator_list=[])

        def visit_Module(self, node):
            self.generic_visit(node)
            if not self.injected:
                node.body.insert(0, self.coder())
                self.injected = True
            return node

        def visit_Constant(self, node):
            if not isinstance(node.value, str):return node
            if not node.value:return node
            try:raw = node.value.encode('utf-8', '✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧')
            except Exception:return node
            encoded = eval(f"getattr(__import__('base64'),'b85encode')(raw)")
            encoded_str = str(encoded, 'ascii')
            mapped = ''.join((self.enc_map.get(c, c) for c in encoded_str))
            return ast.Call(func=ast.Name(id=self.sothatday, ctx=ast.Load()), args=[ast.Constant(mapped)], keywords=[])
    transformer = __chanbomayde__()
    code = transformer.visit(code)
    ast.fix_missing_locations(code)
    return code

def speed2(code):
    code = ast.parse(code) if isinstance(code, str) else code
    class UnicodeObf(ast.NodeTransformer):

        def __init__(self):
            self.injected = False
            self.sothatday = f'__{nghich}___'

        def visit_JoinedStr(self, node):
            return node

        def obfstringv1(self):
            namanhdzai = f'{_ord}'
            thgchongu = f'_{thicthamcrush}'
            nolatheo = ''.join(map(chr, [106, 111, 105, 110]))
            return ast.FunctionDef(name=self.sothatday, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=f'{x}'), ast.arg(arg=f'{o}')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ast.Return(value=ast.Call(func=ast.Attribute(value=ast.Constant(''), attr=nolatheo, ctx=ast.Load()), args=[ast.GeneratorExp(elt=ast.Call(func=ast.Name(id=thgchongu, ctx=ast.Load()), args=[ast.BinOp(left=ast.Call(func=ast.Name(id=namanhdzai, ctx=ast.Load()), args=[ast.Name(id=f'{c}', ctx=ast.Load())], keywords=[]), op=ast.Sub(), right=ast.Name(id=f'{o}', ctx=ast.Load()))], keywords=[]), generators=[ast.comprehension(target=ast.Name(id=f'{c}', ctx=ast.Store()), iter=ast.Name(id=f'{x}', ctx=ast.Load()), ifs=[], is_async=0)])], keywords=[]))], decorator_list=[])

        def visit_Module(self, node):
            self.generic_visit(node)
            if not self.injected:
                node.body.insert(0, self.obfstringv1())
                self.injected = True
            return node

        def visit_Constant(self, node):
            if not isinstance(node.value, str):
                return node
            if not node.value:
                return node
            OFFSET = random.randint(*random.choice([(128544, 128549), (1000, 3000), (768, 879)]))
            mahoanangcao = ''.join((chr(ord(c) + OFFSET) for c in node.value))
            a = random.randint(44032, 55204)
            b = random.randint(1000, 3000)
            thuatchunganh = (a + b) - OFFSET
            expr = f"((lambda: ({hex(a)}+{hex(b)}))())-((lambda: {hex(thuatchunganh)})())"
            ToLaAbyss = f'\\({expr})'
            obf_offset = ast.Call(func=ast.Name(id=f'{champ}',ctx=ast.Load()),args=[ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[],args=[],kwonlyargs=[],kw_defaults=[],defaults=[]),body=ast.Constant(str(ToLaAbyss[1:]))),args=[],keywords=[])],keywords=[])
            return ast.Call(func=ast.Name(id=self.sothatday, ctx=ast.Load()), args=[ast.Constant(mahoanangcao), obf_offset], keywords=[])
    transformer = UnicodeObf()
    code = transformer.visit(code)
    ast.fix_missing_locations(code)
    return code

def speed3(code):
    code = ast.parse(code) if isinstance(code, str) else code

    class UnicodeObf(ast.NodeTransformer):

        def __init__(self):
            self.injected = False
            self.sothatday = f'__{nghich1}___'

        def visit_JoinedStr(self, node):
            return node

        def phanoffset(self, n):
            return ''.join((chr(0x1F300 + (n >> i & 15)) for i in range(0, 16, 4)))

        def okdecode(self):
            return ast.Call(func=ast.Name(id=f'{_sum}', ctx=ast.Load()), args=[ast.GeneratorExp(elt=ast.BinOp(left=ast.BinOp(left=ast.Call(func=ast.Name(id=f'{_ord}', ctx=ast.Load()), args=[ast.Name(id=f'{c}', ctx=ast.Load())], keywords=[]), op=ast.Sub(), right=ast.Name(id='CauBiLuaRoii', ctx=ast.Load())), op=ast.LShift(), right=ast.BinOp(left=ast.Name(id=f'{i}', ctx=ast.Load()), op=ast.Mult(), right=ast.Constant(4))), generators=[ast.comprehension(target=ast.Tuple(elts=[ast.Name(id=f'{i}', ctx=ast.Store()), ast.Name(id=f'{c}', ctx=ast.Store())], ctx=ast.Store()), iter=ast.Call(func=ast.Name(id='_0x4', ctx=ast.Load()), args=[ast.Name(id='TroiMaThatKhongDa', ctx=ast.Load())], keywords=[]), ifs=[], is_async=0)])], keywords=[])

        def obfstringv1(self):
            x = f'{_ord}' + nghich1
            z = f'_{_ord}' + nghich1
            c = f'__{_ord}' + nghich1
            return ast.FunctionDef(name=self.sothatday, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=x), ast.arg(arg='__BoLaHacAm__'), ast.arg(arg='__TayChaySuNghiep__'), ast.arg(arg='__TamBietNheToiQuaMetMoi__'), ast.arg(arg='TroiMaThatKhongDa')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ast.Return(value=ast.Call(func=ast.Attribute(value=ast.Constant(''), attr='join', ctx=ast.Load()), args=[ast.GeneratorExp(elt=ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=z)], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.Call(func=ast.Attribute(value=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.Call(func=ast.Name(id=f'{_ord}', ctx=ast.Load()), args=[ast.Name(id=z, ctx=ast.Load())], keywords=[]), op=ast.Sub(), right=self.okdecode()), op=ast.BitXor(), right=ast.Call(func=ast.Name(id='__KhangCoder__', ctx=ast.Load()), args=[ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id='__TayChaySuNghiep__', ctx=ast.Load()), ast.Name(id=f'{_replace}', ctx=ast.Load())], keywords=[]), args=[ast.Name(id=f'{_uni}({anhxa1("PyTiㅤAbi/")})', ctx=ast.Load()), ast.Name(id='ToiㅤYeuㅤEmㅤNhieuㅤLam', ctx=ast.Load())], keywords=[]), ast.Name(id=f'{_aychochoco}', ctx=ast.Load())], keywords=[])), op=ast.Sub(), right=ast.Call(func=ast.Name(id='__KhangCoder__', ctx=ast.Load()), args=[ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id='__TamBietNheToiQuaMetMoi__', ctx=ast.Load()), ast.Name(id=f'{_replace}', ctx=ast.Load())], keywords=[]), args=[ast.Name(id=f'{_uni}({anhxa1("PyTiㅤAbi/")})', ctx=ast.Load()), ast.Name(id='ToiㅤYeuㅤEmㅤNhieuㅤLam', ctx=ast.Load())], keywords=[]), ast.Name(id=f'{_aychochoco}', ctx=ast.Load())], keywords=[])), op=ast.BitXor(), right=ast.Call(func=ast.Name(id='__KhangCoder__', ctx=ast.Load()), args=[ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id='__BoLaHacAm__', ctx=ast.Load()), ast.Name(id=f'{_replace}', ctx=ast.Load())], keywords=[]), args=[ast.Name(id=f'{_uni}({anhxa1("PyTiㅤAbi/")})', ctx=ast.Load()), ast.Name(id='ToiㅤYeuㅤEmㅤNhieuㅤLam', ctx=ast.Load())], keywords=[]), ast.Name(id=f'{_aychochoco}', ctx=ast.Load())], keywords=[])), attr='__format__', ctx=ast.Load()), args=[ast.Name(id=f'{_c}', ctx=ast.Load())], keywords=[])), args=[ast.Name(id=c, ctx=ast.Load())], keywords=[]), generators=[ast.comprehension(target=ast.Name(id=c, ctx=ast.Store()), iter=ast.Name(id=x, ctx=ast.Load()), ifs=[], is_async=0)])], keywords=[]))], decorator_list=[])

        def visit_Module(self, node):
            self.generic_visit(node)
            if not self.injected:
                node.body.insert(0, self.obfstringv1())
                self.injected = True
            return node

        def visit_Constant(self, node):
            if not isinstance(node.value, str) or not node.value:
                return node
            __BoLaHacAm__ = random.randint(10000, 99999)
            __TayChaySuNghiep__ = random.randint(1000, 9999)
            __TamBietNheToiQuaMetMoi__ = random.randint(100, 999)
            NgaoLol = random.randint(1000, 3000)
            NgaoLol_enc = self.phanoffset(NgaoLol)
            encoded = ''.join((chr(((ord(c) ^ __BoLaHacAm__) + __TamBietNheToiQuaMetMoi__ ^ __TayChaySuNghiep__) + NgaoLol) for c in node.value))
            return ast.Call(func=ast.Name(id=self.sothatday,ctx=ast.Load()),args=[ast.Constant(encoded),ast.Constant(f'PyTiㅤAbi/{hex(__BoLaHacAm__)}'),ast.Constant(f'PyTiㅤAbi/{hex(__TayChaySuNghiep__)}'),ast.Constant(f'PyTiㅤAbi/{hex(__TamBietNheToiQuaMetMoi__)}'),ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[],args=[],kwonlyargs=[],kw_defaults=[],defaults=[]),body=ast.Name(id=f'("{NgaoLol_enc}")', ctx=ast.Load())),args=[],keywords=[])],keywords=[])
    transformer = UnicodeObf()
    code = transformer.visit(code)
    ast.fix_missing_locations(code)
    return code

bavailonctevcl = ''.join(random.sample([chr(i) for i in range(19968, 40959)], 2))
bavailonctevcl1 = ''.join(random.sample([chr(i) for i in range(19968, 40959)], 5))
def __xamlolthoi__(code):
    tree = ast.parse(code)
    # FIX: preserve 'from __future__' at top - don't wrap with junk
    _fut = [n for n in tree.body if isinstance(n, ast.ImportFrom) and n.module == '__future__']
    _rest = [n for n in tree.body if n not in _fut]
    if _fut:
        if _rest:
            _rt = ast.Module(body=_rest, type_ignores=[])
            _rt = hide().visit(_rt)
            _rt.body = sieucaplongjunk(_rt.body, 1)
            ast.fix_missing_locations(_rt)
            tree.body = _fut + _rt.body
        else:
            # only future imports, just hide (no junk)
            tree = hide().visit(tree)
        ast.fix_missing_locations(tree)
        return ast.unparse(tree)
    tree = hide().visit(tree)
    tree.body = sieucaplongjunk(tree.body, 1)
    ast.fix_missing_locations(tree)
    return ast.unparse(tree)

import string as meo
__daucau_an_toan__ = meo.punctuation.replace('"', '').replace('\\', '')
__cothenoilaratngau__ = meo.ascii_lowercase + meo.digits + meo.ascii_uppercase + meo.hexdigits + __daucau_an_toan__

def _fix_future_imports_src(src: str) -> str:
    # FIX: 'from __future__ imports must occur at beginning' - reorder to top
    if not isinstance(src, str) or 'from __future__' not in src:
        return src
    try:
        tree = ast.parse(src)
    except SyntaxError:
        # fallback text-based reorder
        try:
            lines = src.splitlines()
            fut = [l for l in lines if l.strip().startswith('from __future__')]
            if not fut:
                return src
            rest = [l for l in lines if not l.strip().startswith('from __future__')]
            # keep encoding/shebang/docstring at very top? keep first line if #!
            return '\n'.join(fut + rest)
        except Exception:
            return src
    body = tree.body
    doc = None
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
        doc = body[0]
        body = body[1:]
    futures = [n for n in body if isinstance(n, ast.ImportFrom) and n.module == '__future__']
    if not futures:
        return src
    others = [n for n in body if n not in futures]
    new_body = []
    if doc is not None:
        new_body.append(doc)
    new_body.extend(futures)
    new_body.extend(others)
    try:
        new_tree = ast.Module(body=new_body, type_ignores=[])
        ast.fix_missing_locations(new_tree)
        return ast.unparse(new_tree)
    except Exception:
        return src

def _fix_future_in_ast(mod):
    # FIX AST: reorder future imports to top before compile
    try:
        if not isinstance(mod, ast.Module):
            return mod
        body = mod.body
        doc = None
        if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
            doc = body[0]
            body = body[1:]
        fut = [n for n in body if isinstance(n, ast.ImportFrom) and getattr(n, 'module', None) == '__future__']
        if not fut:
            return mod
        rest = [n for n in body if n not in fut]
        new_body = []
        if doc is not None:
            new_body.append(doc)
        new_body.extend(fut)
        new_body.extend(rest)
        mod.body = new_body
        ast.fix_missing_locations(mod)
    except Exception:
        pass
    return mod

def obflzmain(metmoi):
    if not metmoi:return '""'
    metmoi=metmoi if isinstance(metmoi,str) else ''
    metmoi = _fix_future_imports_src(metmoi)
    try:
        codeobj = compile(metmoi,'ProJect','exec')
    except SyntaxError as _e:
        if 'from __future__' in str(_e):
            # text fallback: move all future imports to top
            lines = metmoi.splitlines()
            fut = [l for l in lines if l.strip().startswith('from __future__')]
            rest = [l for l in lines if not l.strip().startswith('from __future__')]
            metmoi2 = '\n'.join(fut + rest)
            codeobj = compile(metmoi2,'ProJect','exec')
            metmoi = metmoi2
        else:
            raise
    dump = marshal.dumps(codeobj)
    dump = lzma.compress(dump)
    dump = dump.hex()
    khocdi = ''.join((secrets.choice(__cothenoilaratngau__) for _ in dump))
    raw = ''.join((a + b for a, b in zip(khocdi, dump)))
    __map__ = {chr(i): chr((i + 7) % 256) for i in range(256)}
    nen = ''.join((__map__.get(i, i) for i in raw)).encode()
    __ok__ = random.randint(25, 60)
    parts = [nen[i:i + __ok__] for i in range(0, len(nen), __ok__)]
    phanmanh = 'b"".join([' + ','.join((repr(p) for p in parts)) + '])'
    return f"""
try:
    (_0xFx4B5.__setitem__({_uni}({anhxa1('ViThanBienCaBaDao')}), {phanmanh}),
    _Ox3.__setitem__({_uni}({anhxa1('SocLoBanZoLon')}), {anhxa1('decompress')}),
    _Ox3.__setitem__({_uni}({anhxa1('SócLọBănZôLồn')}), {anhxa1('join')}),
    _Ox3.__setitem__(___BoMayLaHeHe__({anhxa('MộtTừThôi')}), {anhxa1('decode')}))
except:
    raise MemoryError
else:
    pass
try:
    _0xFx4B5[{_uni}({anhxa1('CoBaoXaRoiBoTaThatLauu')})]=KhangCoder(DungCoDecNuaAnhOi).__getattribute__({_uni}(ThậtBuồnCười))(KhangCoder(DungCoDecNuaAnhOi1).__getattribute__({_uni}(SocLoBanZoLon))(getattr(getattr(KhangCoder({enc('builtins')}),___BoMayLaHeHe__({anhxa('bytes')})),{enc('fromhex')})((KyThuatAnCode.__getattribute__({_uni}(SócLọBănZôLồn))(_{thicthamcrush}((NgaoChoDaiDoanCuoi({c})-ToiㅤCoㅤUocㅤThanhㅤ1ㅤNhacㅤSiㅤNoiㅤLoan)%BoLaLoVuongHahah)for {c} in ViThanBienCaBaDao.__getattribute__({_uni}(MộtTừThôi))()))[(ToLaBuaYeu^No1)::(ToLaBuaYeu<<ToLaBuaYeu)])))
except:
    raise MemoryError
else:
    pass
KhangCoder({enc('builtins')}).__getattribute__({enc('exec')})(CoBaoXaRoiBoTaThatLauu,_0xFx4B5)"""

__daucau_an_toan__=meo.punctuation.replace('"','').replace('\\','')
__cothenoilaratngau__=meo.ascii_lowercase+meo.digits+meo.ascii_uppercase+meo.hexdigits+__daucau_an_toan__
def obflzexec(metmoi):
    if not metmoi:return '""'
    metmoi=metmoi if isinstance(metmoi,str) else ''
    tambo=metmoi.encode().hex()
    khocdi=''.join(secrets.choice(__cothenoilaratngau__)for _ in tambo)
    raw=''.join(a+b for a,b in zip(khocdi,tambo))
    __map__={chr(i):chr((i+7)%256) for i in range(256)}
    nen=''.join(__map__.get(i,i) for i in raw).encode()
    __ok__=random.randint(25,60)
    parts=[nen[i:i+__ok__] for i in range(0,len(nen),__ok__)]
    phanmanh='b"".join(['+','.join(repr(p) for p in parts)+'])'
    return f"""try:
    (_Ox3.__setitem__({_uni}({anhxa1(fr"{bavailonctevcl}")}), {phanmanh}), _0xFx4B5.__setitem__({_uni}({anhxa1('GioiThiDeobfDi')}), {anhxa('decode')}))
except:
    raise MemoryError
else:
    pass
try:
    globals()[___BoMayLaHeHe__({anhxa('BeuBeBongDangiu')})]={_uni}({anhxa1('exec')});_0xFx4B5[{_uni}({anhxa1('GoJoSaToRu')})]={anhxa('join')}
except:
    raise MemoryError
else:
    pass
ThapChungAnhLevel1000=getattr(KhangCoder(___BoMayLaHeHe__({anhxa('builtins')})),BeuBeBongDangiu)((lambda {kwds}:getattr(getattr(getattr(KhangCoder(___BoMayLaHeHe__({anhxa('builtins')})),LuaGaTreCon),{_uni}({anhxa1('fromhex')}))({kwds}),{_uni}({anhxa1('decode')}))())((lambda {t}:getattr(KyThuatAnCode,___BoMayLaHeHe__(GoJoSaToRu))(_{thicthamcrush}((NgaoChoDaiDoanCuoi({_str})-ToiㅤCoㅤUocㅤThanhㅤ1ㅤNhacㅤSiㅤNoiㅤLoan)%BoLaLoVuongHahah)for {_str} in {t}))(getattr(KhangCoder(___BoMayLaHeHe__({anhxa('builtins')})),LuaGaTreCon)({bavailonctevcl}).__getattribute__(___BoMayLaHeHe__(GioiThiDeobfDi))())[(ToLaBuaYeu^No1)::(ToLaBuaYeu<<ToLaBuaYeu)]),_0xFx4B5)
try:
    PyTi_Abi_That_Dang_Iu({enc('ThapChungAnhLevel1000')})
except:
    raise MemoryError
else:
    pass"""

__daucau_an_toan__=meo.punctuation.replace('"','').replace('\\','')
__cothenoilaratngau__=meo.ascii_lowercase+meo.digits+meo.ascii_uppercase+meo.hexdigits+__daucau_an_toan__
def obflzimport(metmoi):
    if not metmoi:return '""'
    metmoi=metmoi if isinstance(metmoi,str) else ''
    metmoi = _fix_future_imports_src(metmoi)
    try:
        codeobj = compile(metmoi,'ProJect','exec')
    except SyntaxError as _e:
        if 'from __future__' in str(_e):
            lines = metmoi.splitlines()
            fut = [l for l in lines if l.strip().startswith('from __future__')]
            rest = [l for l in lines if not l.strip().startswith('from __future__')]
            metmoi2 = '\n'.join(fut + rest)
            codeobj = compile(metmoi2,'ProJect','exec')
            metmoi = metmoi2
        else:
            raise
    dump = marshal.dumps(codeobj)
    dump = lzma.compress(dump)
    dump = dump.hex()
    khocdi=''.join(secrets.choice(__cothenoilaratngau__)for _ in dump)
    raw=''.join(a+b for a,b in zip(khocdi,dump))
    __map__={chr(i):chr((i+7)%256) for i in range(256)}
    nen=''.join(__map__.get(i,i) for i in raw).encode()
    __ok__=random.randint(25,60)
    parts=[nen[i:i+__ok__] for i in range(0,len(nen),__ok__)]
    phanmanh='b"".join(['+','.join(repr(p) for p in parts)+'])'
    return f"""try:
    (_0xFx4B5.__setitem__({_uni}({anhxa1('ViThanBienCaBaDao1')}), {phanmanh}),
    _Ox3.__setitem__({_uni}({anhxa1('SocLoBanZoLon1')}), {anhxa1('decompress')}),
    _Ox3.__setitem__({_uni}({anhxa1('SócLọBănZôLồn1')}), {anhxa1('join')}),
    _Ox3.__setitem__(___BoMayLaHeHe__({anhxa('MộtTừThôi1')}), {anhxa1('decode')}))
except:
    raise MemoryError
else:
    pass
try:
    _0xFx4B5[{_uni}({anhxa1('CoBaoXaRoiBoTaThatLauu1')})]=KhangCoder(DungCoDecNuaAnhOi).__getattribute__({_uni}(ThậtBuồnCười))(KhangCoder(DungCoDecNuaAnhOi1).__getattribute__({_uni}(SocLoBanZoLon1))(getattr(getattr(KhangCoder({enc('builtins')}),___BoMayLaHeHe__({anhxa('bytes')})),{enc('fromhex')})((KyThuatAnCode.__getattribute__({_uni}(SócLọBănZôLồn1))(_{thicthamcrush}((NgaoChoDaiDoanCuoi({c})-ToiㅤCoㅤUocㅤThanhㅤ1ㅤNhacㅤSiㅤNoiㅤLoan)%BoLaLoVuongHahah)for {c} in ViThanBienCaBaDao1.__getattribute__({_uni}(MộtTừThôi1))()))[(ToLaBuaYeu^No1)::(ToLaBuaYeu<<ToLaBuaYeu)])))
except:
    raise MemoryError
else:
    pass
KhangCoder({enc('types')}).__getattribute__({_uni}({anhxa1('FunctionType')}))(CoBaoXaRoiBoTaThatLauu1,_0xFx4B5)()"""

mapping = ['你', ' ']
autodeobf = ['\u200b', '\u200d']
def obfsieumanh(s: str):
    if not s:return ast.Constant(value='')
    sep = random.choice(autodeobf)
    parts = []
    for c in s:
        num = str(ord(c) * 3)
        num += ''.join((random.choice(mapping) for _ in range(random.randint(1, 5))))
        parts.append(num)
    encoded = sep.join(parts)
    code = f"""getattr(KhangCoder(___BoMayLaHeHe__({anhxa('builtins')})),{enc('str')})().__getattribute__({_uni}({anhxa1('join')}))(getattr(KhangCoder({_uni}({anhxa1('builtins')})),
___BoMayLaHeHe__({anhxa('chr')}))(getattr(KhangCoder(___BoMayLaHeHe__({anhxa('builtins')})),
{enc('int')})(getattr(KhangCoder({enc('builtins')}),
{enc('str')})().join(getattr(KhangCoder({enc('builtins')}),
{enc('filter')})(getattr(getattr(KhangCoder({enc('builtins')}),
{enc('str')}),
{enc('isdigit')}),
{c})))//XinChaoVietNam)for {c} in getattr(getattr(KhangCoder({enc('builtins')}),
{enc('str')})({enc(encoded)}),{enc('split')})(getattr(KhangCoder({enc('builtins')}),
{enc('str')})({enc(sep)})))"""
    return ast.parse(code).body[0].value

import string as meo1
__daucau_an_toan__ = meo1.punctuation.replace('"', '').replace('\\', '')
__cothenoilaratngau__ = meo1.ascii_lowercase + meo1.digits + meo1.ascii_uppercase + meo1.hexdigits + __daucau_an_toan__

def obflz1(metmoi, __depth__ = 1):
    if not metmoi:
        return '""'
    metmoi = _fix_future_imports_src(metmoi)
    try:
        codeobj = compile(metmoi, 'ProJect', 'exec')
    except SyntaxError as _e:
        if 'from __future__' in str(_e):
            lines = metmoi.splitlines()
            fut = [l for l in lines if l.strip().startswith('from __future__')]
            rest = [l for l in lines if not l.strip().startswith('from __future__')]
            metmoi2 = '\n'.join(fut + rest)
            codeobj = compile(metmoi2,'ProJect','exec')
            metmoi = metmoi2
        else:
            raise
    data = marshal.dumps(codeobj)
    for _ in range(__depth__):
        data = lzma.compress(data)
        data = marshal.dumps(data)
    tambo = data.hex()
    khocdi = ''.join((secrets.choice(__cothenoilaratngau__) for _ in tambo))
    raw = ''.join((a + b for a, b in zip(khocdi, tambo)))
    nen = lzma.compress(raw.encode())
    __fake1__ = random.randbytes(random.randint(10, 30))
    __fake2__ = random.randbytes(random.randint(20, 50))
    __that__ = __fake1__ + nen + __fake2__
    __qualohaha__ = len(__fake1__)
    __end__ = len(__that__) - len(__fake2__)
    __ok__ = random.randint(1000, 3000)
    parts = [__that__[i:i + __ok__] for i in range(0, len(__that__), __ok__)]
    phanmanh = 'b"".join([' + ','.join((repr(p) for p in parts)) + '])'
    __v1__ = rb()
    __v2__ = rb()
    __v3__ = rb()
    __v4__ = rb()
    final_expr = f"(KhangCoder({enc('types')}).__getattribute__({enc('FunctionType')})((lambda {__v1__}:(lambda {__v2__},{__v3__}:{__v1__}({__v1__},{__v2__},{__v3__})))(lambda {__v4__},{__v2__},{__v3__}:{__v4__}({__v4__},getattr(KhangCoder({enc('lzma')}), {enc('decompress')})(getattr(KhangCoder({enc('marshal')}),{enc('loads')})({__v2__})),{__v3__}-ToLaBuaYeu) if {__v3__}> No1 else getattr(KhangCoder({enc('marshal')}),{enc('loads')})({__v2__}))((lambda {kwds}:getattr(getattr(KhangCoder({enc('builtins')}),LuaGaTreCon),{enc('fromhex')})({kwds}))((lambda {x}:{x}[ToLaBuaYeu::ToLaBuaYeu1])(getattr(KhangCoder({enc('lzma')}),{enc('decompress')})(__XxXPyTiXxAbiXxX__[{__qualohaha__!r}:{__end__!r}]).__getattribute__({enc('decode')})({enc('latin1')}))),{__depth__}),_Ox3))()"
    return f"""
try:
    _Ox3[{enc('__XxXPyTiXxAbiXxX__')}]={champ}({sieugaylomalaihay(phanmanh)})
except:
    raise MemoryError
else:
    {final_expr}"""

dark = Col.dark_gray
light = Col.light_gray
def stage(text: str, symbol: str = '>>', col1=None) -> str:
    if col1 is None:
        col1 = light
    return f"\n{Col.Symbol(symbol, col1, dark)} {text}{light}"
def stage1(text: str, symbol: str = '>>', col1=None) -> str:
    if col1 is None:
        col1 = light
    return f"{Col.Symbol(symbol, col1, dark)} {text}{light}"
def stage2(text: str, symbol: str = '>>', col1=None) -> str:
    if col1 is None:
        col1 = light
    return f"{Col.Symbol(symbol, col1, dark)} {text}{light}"
def stage3(text: str, symbol: str = '>>', col1=None) -> str:
    if col1 is None:
        col1 = light
    return f"{Col.Symbol(symbol, col1, dark)} {text}{light}"

class pro(ast.NodeTransformer):

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            return obfsieumanh(node.value)
        return node

# === ENHANCED URL HIDE v2 + REQUESTS HIDE v2 - ALWAYS ON - POLYMORPHIC ===
import re as _re_url_hide
import base64 as _b64_url_hide
import zlib as _zlib_url_hide
import string as _str_url_hide
import uuid as _uuid_url_hide

_PYTI_URL_DECODER_NAME = f'__PyTi_Url_{_uuid_url_hide.uuid4().hex[:8]}__'
_PYTI_URL_DECODER_CURRENT = _PYTI_URL_DECODER_NAME
_PYTI_URL_PATTERNS = ('http://', 'https://', 'ftp://', 'wss://', 'ws://', 'www.')
_PYTI_URL_KEYWORDS = ('api','cdn','webhook','bot','github','discord','telegram','ngrok','t.me','pastebin','raw.github','discordapp','hooks.slack','openai','/v1','/v2','/v3','.io/','.com/','.net/','.org/','.xyz/','.onion/','.dev/','.app/')
_PYTI_REQUESTS_STRINGS = ('requests','urllib3','http.client','socket','urllib.request','urllib.parse','requests.sessions','requests.adapters','Session','HTTPAdapter','urlopen','getaddrinfo','gethostbyname','connect','send','request','get','post','put','delete','patch','head','options')

_re_url_hide_domain = _re_url_hide.compile(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.[a-z]{2,}(?:/|\b)', _re_url_hide.I)
_re_url_hide_ip = _re_url_hide.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?::\d{1,5})?\b')
_re_url_hide_url = _re_url_hide.compile(r'https?://|ftp://|wss?://|www\.', _re_url_hide.I)

def _is_url_string(s: str) -> bool:
    if not isinstance(s, str):
        return False
    if not s or len(s) < 4 or len(s) > 2048:
        return False
    ls = s.lower()
    if any(p in ls for p in _PYTI_URL_PATTERNS):
        return True
    if _re_url_hide_url.search(ls):
        return True
    if _re_url_hide_ip.search(ls):
        return True
    has_keyword = any(k in ls for k in _PYTI_URL_KEYWORDS)
    has_domain = _re_url_hide_domain.search(ls) is not None
    has_slash = '/' in ls or ':' in ls
    if has_domain and (has_slash or has_keyword):
        return True
    if has_keyword and has_slash and '.' in ls:
        return True
    if _re_url_hide.search(r'[a-z0-9]{2,}\.[a-z]{2,}/', ls) and ('api' in ls or 'cdn' in ls or '/v' in ls or 'webhook' in ls or 'bot' in ls):
        return True
    return False

def _is_requests_string(s: str) -> bool:
    if not isinstance(s, str):
        return False
    return s in _PYTI_REQUESTS_STRINGS or s.lower() in ('requests','urllib3','socket')

def _encode_url_for_hide(s: str) -> str:
    # FIX BUG #3: per-build XOR/ROT keys (no static 0x5A / 13 fingerprint).
    try:
        idx = random.randint(0, 4)
        data = s.encode('utf-8')
        if idx == 0:
            payload = _b64_url_hide.b85encode(_zlib_url_hide.compress(data, 9)).decode('ascii')
        elif idx == 1:
            payload = _b64_url_hide.b64encode(_zlib_url_hide.compress(data, 9)).decode('ascii')
        elif idx == 2:
            payload = _b64_url_hide.b64encode(data).decode('ascii')
        elif idx == 3:
            xored = bytes(b ^ (_PYTI_URL_XOR & 0xFF) for b in data)
            payload = _b64_url_hide.b85encode(xored).decode('ascii')
        else:
            _rr = _PYTI_URL_ROT % 95
            rot = bytes(((b - 32 + _rr) % 95 + 32) if 32 <= b <= 126 else b for b in data)
            payload = _b64_url_hide.b64encode(rot).decode('ascii')
        return f"{idx}:{payload}"
    except:
        try:
            return "2:" + _b64_url_hide.b64encode(s.encode()).decode()
        except:
            return "2:" + s

def _collect_binop_strings(node):
    parts = []
    def _recurse(n):
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            parts.append(n.value)
            return True
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):
            return _recurse(n.left) and _recurse(n.right)
        return False
    if _recurse(node):
        def _collect_order(n):
            if isinstance(n, ast.Constant):
                return [n.value]
            if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):
                return _collect_order(n.left) + _collect_order(n.right)
            return []
        ordered = _collect_order(node)
        return ''.join(ordered)
    return None

class UrlHideTransformer(ast.NodeTransformer):
    def __init__(self, decoder_name=None):
        self.decoder = decoder_name or _PYTI_URL_DECODER_CURRENT
        super().__init__()
    def visit_Constant(self, node):
        if isinstance(node.value, str) and _is_url_string(node.value):
            enc = _encode_url_for_hide(node.value)
            return ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])
        if isinstance(node.value, bytes) and _is_url_string(node.value.decode('utf-8', errors='ignore')):
            try:
                s = node.value.decode('utf-8')
                enc = _encode_url_for_hide(s)
                return ast.Call(func=ast.Attribute(value=ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[]), attr='encode', ctx=ast.Load()), args=[], keywords=[])
            except:
                pass
        if isinstance(node.value, str) and _is_requests_string(node.value):
            if not _is_url_string(node.value):
                enc = _encode_url_for_hide(node.value)
                return ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])
        return node
    def visit_JoinedStr(self, node):
        for idx, v in enumerate(getattr(node, 'values', [])):
            if isinstance(v, ast.Constant) and isinstance(v.value, str) and _is_url_string(v.value):
                enc = _encode_url_for_hide(v.value)
                node.values[idx] = ast.FormattedValue(value=ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[]), conversion=-1)
            elif isinstance(v, ast.FormattedValue):
                if isinstance(v.value, ast.Constant) and isinstance(v.value.value, str) and _is_url_string(v.value.value):
                    enc = _encode_url_for_hide(v.value.value)
                    v.value = ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])
        return self.generic_visit(node)
    def visit_BinOp(self, node):
        # Check BEFORE visiting children to catch 'https://' + 'example.com' chain before individual Constants are encoded
        combined = _collect_binop_strings(node)
        if combined and _is_url_string(combined):
            enc = _encode_url_for_hide(combined)
            return ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])
        self.generic_visit(node)
        # Also check after visiting for already partially encoded? re-check
        combined2 = _collect_binop_strings(node)
        if combined2 and _is_url_string(combined2):
            enc = _encode_url_for_hide(combined2)
            return ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])
        return node
    def visit_Dict(self, node):
        self.generic_visit(node)
        return node
    def visit_List(self, node):
        self.generic_visit(node)
        return node
    def visit_Tuple(self, node):
        self.generic_visit(node)
        return node
    def visit_Call(self, node):
        self.generic_visit(node)
        # hide url in kwargs like url=, uri=, endpoint=, host=, domain=
        for kw in node.keywords:
            if kw.arg in ('url','uri','endpoint','host','domain','hostname','server') and isinstance(kw.value, ast.BinOp):
                combined = _collect_binop_strings(kw.value)
                if combined and _is_url_string(combined):
                    enc = _encode_url_for_hide(combined)
                    kw.value = ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])
            # also hide Constant hostnames in kwargs like host='example.com'
            if kw.arg in ('host','hostname','domain','server') and isinstance(kw.value, ast.Constant) and isinstance(kw.value.value, str):
                if _is_url_string(kw.value.value) or _re_url_hide_domain.search(kw.value.value):
                    enc = _encode_url_for_hide(kw.value.value)
                    kw.value = ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])
        if node.args:
            arg0 = node.args[0]
            if isinstance(arg0, ast.BinOp):
                combined = _collect_binop_strings(arg0)
                if combined and _is_url_string(combined):
                    enc = _encode_url_for_hide(combined)
                    node.args[0] = ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])
            # hide standalone host like getaddrinfo('example.com', 80)
            if isinstance(arg0, ast.Constant) and isinstance(arg0.value, str):
                if _re_url_hide_domain.search(arg0.value) and '.' in arg0.value and len(arg0.value) > 4:
                    # check if parent is getaddrinfo/gethostbyname
                    try:
                        func_name = ""
                        if isinstance(node.func, ast.Attribute):
                            func_name = node.func.attr
                        elif isinstance(node.func, ast.Name):
                            func_name = node.func.id
                        if func_name in ('getaddrinfo','gethostbyname','gethostbyname_ex','create_connection'):
                            enc = _encode_url_for_hide(arg0.value)
                            node.args[0] = ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])
                    except:
                        pass
        return node

def inject_url_decoder(tree: ast.Module, decoder_name=None):
    # FIX BUG #3: polymorphic decoder - per-build XOR/ROT, indirect imports (anti-grep),
    # dispatch-dict + opaque predicate (no static 5-branch plaintext fingerprint).
    if decoder_name is None:
        decoder_name = _PYTI_URL_DECODER_CURRENT
        if random.random() < 0.3:
            decoder_name = f'__PyTi_Url_{_uuid_url_hide.uuid4().hex[:6]}__'
    _ux = _PYTI_URL_XOR & 0xFF
    _ur = _PYTI_URL_ROT % 95
    # indirect import expressions to avoid greppable 'import base64/zlib'
    _imp_b64_e = _pyti_chr_expr('base64')
    _imp_zl_e = _pyti_chr_expr('zlib')
    _a = f'_a{uuid.uuid4().hex[:4]}'
    _b = f'_b{uuid.uuid4().hex[:4]}'
    src_lines = []
    src_lines.append(f"def {decoder_name}(__enc__):")
    src_lines.append(f"    try:")
    src_lines.append(f"        {_a}=__import__({_imp_b64_e});{_b}=__import__({_imp_zl_e})")
    src_lines.append(f"        __b64d__, __zl__ = {_a}, {_b}")
    src_lines.append(f"        del {_a}, {_b}")
    src_lines.append(f"        try:")
    src_lines.append(f"            if isinstance(__enc__, str) and \":\" in __enc__:")
    src_lines.append(f"                __idx__, __payload__ = __enc__.split(\":\", 1)")
    src_lines.append(f"                __idx__ = int(__idx__)")
    src_lines.append(f"            else:")
    src_lines.append(f"                __idx__, __payload__ = 0, __enc__")
    src_lines.append(f"            if (len(__enc__) * 2654435761 & 0xFFFFFFFF) == 0xDEADBEEF:")
    src_lines.append(f"                return __enc__")
    src_lines.append(f"            __dispatch__ = {{0: 'z_b85', 1: 'z_b64', 2: 'b64', 3: 'xor', 4: 'rot'}}")
    src_lines.append(f"            __kind__ = __dispatch__.get(__idx__, 'raw')")
    src_lines.append(f"            if __kind__ == 'z_b85':")
    src_lines.append(f"                return __zl__.decompress(__b64d__.b85decode(__payload__.encode('ascii'))).decode('utf-8', errors='ignore')")
    src_lines.append(f"            elif __kind__ == 'z_b64':")
    src_lines.append(f"                return __zl__.decompress(__b64d__.b64decode(__payload__.encode('ascii'))).decode('utf-8', errors='ignore')")
    src_lines.append(f"            elif __kind__ == 'b64':")
    src_lines.append(f"                return __b64d__.b64decode(__payload__.encode('ascii')).decode('utf-8', errors='ignore')")
    src_lines.append(f"            elif __kind__ == 'xor':")
    src_lines.append(f"                __xored__ = __b64d__.b85decode(__payload__.encode('ascii'))")
    src_lines.append(f"                return bytes(b ^ {_ux} for b in __xored__).decode('utf-8', errors='ignore')")
    src_lines.append(f"            elif __kind__ == 'rot':")
    src_lines.append(f"                __rot__ = __b64d__.b64decode(__payload__.encode('ascii'))")
    src_lines.append(f"                return bytes(((b - 32 - {_ur}) % 95 + 32) if 32 <= b <= 126 else b for b in __rot__).decode('utf-8', errors='ignore')")
    src_lines.append(f"            else:")
    src_lines.append(f"                return __payload__")
    src_lines.append(f"        except:")
    src_lines.append(f"            try:")
    src_lines.append(f"                return __b64d__.b64decode(__enc__.encode()).decode('utf-8', errors='ignore')")
    src_lines.append(f"            except:")
    src_lines.append(f"                return __enc__")
    src_lines.append(f"    except:")
    src_lines.append(f"        return __enc__")
    decoder_src = "\n".join(src_lines)
    try:
        dec_tree = ast.parse(decoder_src)
        tree.body = dec_tree.body + tree.body
        ast.fix_missing_locations(tree)
    except Exception:
        pass
    return tree

def apply_url_hide_always(tree, decoder_name=None):
    try:
        fresh = f'__PyTi_Url_{_uuid_url_hide.uuid4().hex[:7]}__'
        global _PYTI_URL_DECODER_CURRENT
        _PYTI_URL_DECODER_CURRENT = fresh
        tree = inject_url_decoder(tree, decoder_name=fresh)
        tree = UrlHideTransformer(decoder_name=fresh).visit(tree)
        tree = apply_requests_hide(tree, decoder_name=fresh)
        ast.fix_missing_locations(tree)
    except Exception as _e:
        try:
            print(f"[URL-HIDE WARN] {_e}")
        except:
            pass
    return tree

class UrlKwargHideTransformer(ast.NodeTransformer):
    def visit_Call(self, node):
        self.generic_visit(node)
        return node

class RequestsHideTransformer(ast.NodeTransformer):
    def __init__(self, decoder_name=None):
        self.decoder = decoder_name or _PYTI_URL_DECODER_CURRENT
        self.alias_map = {}
        super().__init__()
    def visit_Import(self, node):
        new_body = []
        has_requests = False
        for alias in node.names:
            if alias.name in ('requests','urllib3','urllib.request','http.client','socket'):
                has_requests = True
                enc = _encode_url_for_hide(alias.name)
                asname = alias.asname or alias.name.split('.')[0]
                new_body.append(ast.parse(f"{asname} = __import__({self.decoder}({repr(enc)}))").body[0])
                self.alias_map[alias.name] = asname
            else:
                new_body.append(ast.Import(names=[alias]))
        if has_requests and len(new_body)==1 and isinstance(new_body[0], ast.Assign):
            return new_body[0]
        if has_requests:
            return node
        return node
    def visit_ImportFrom(self, node):
        if node.module in ('requests','urllib3','http.client','urllib.request','socket','requests.sessions','requests.adapters'):
            pass
        return node
    def visit_Attribute(self, node):
        self.generic_visit(node)
        # === BROAD HIDE: any sensitive attr is encoded regardless of base for stealth ===
        _sensitive = ('get','post','put','delete','request','patch','head','options','Session','HTTPAdapter','HTTPConnection','HTTPSConnection','urlopen','getaddrinfo','gethostbyname','gethostbyname_ex','connect','send','sendall','recv','recvfrom','sendto','setsockopt','poolmanager','connectionpool','putrequest','getresponse','endheaders')
        if node.attr in _sensitive:
            base_str = ""
            try:
                base_str = ast.unparse(node.value).lower()
            except:
                try:
                    base_str = getattr(node.value, 'id', '').lower()
                except:
                    base_str = ""
            is_network_base = any(x in base_str for x in ('request','urllib','socket','http','session','adapter','pool','client','conn'))
            is_always_network_attr = node.attr in ('urlopen','getaddrinfo','gethostbyname','connect','send','sendall','recv','Session','HTTPAdapter','HTTPConnection','HTTPSConnection','poolmanager','connectionpool','putrequest','getresponse','request')
            # Always hide 'request' (Session.request) regardless of base - it's rarely dict method
            if node.attr == 'request' or is_always_network_attr:
                enc_attr = _encode_url_for_hide(node.attr)
                return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.value, ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc_attr)], keywords=[])], keywords=[])
            if is_network_base or node.attr in ('get','post','request'):
                if node.attr in ('get','post','put','delete','patch','head','options','request'):
                    if is_network_base or base_str in ('requests','urllib','http','socket') or 'getattr' in base_str:
                        enc_attr = _encode_url_for_hide(node.attr)
                        return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.value, ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc_attr)], keywords=[])], keywords=[])
                    pass
                else:
                    enc_attr = _encode_url_for_hide(node.attr)
                    return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.value, ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc_attr)], keywords=[])], keywords=[])
        # Handle Name.attr for urllib.request etc. (already covered above but keep for completeness)
        if isinstance(node.value, ast.Name) and node.value.id in ('requests','urllib','urllib3','http','socket'):
            if node.attr in ('get','post','put','delete','request','patch','head','options','Session','HTTPAdapter','urlopen','getaddrinfo','gethostbyname','gethostbyname_ex','connect','send','sendall','recv','HTTPConnection','HTTPSConnection','poolmanager','connectionpool','request','putrequest','getresponse','endheaders'):
                enc_attr = _encode_url_for_hide(node.attr)
                return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.value, ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc_attr)], keywords=[])], keywords=[])
        return node

def apply_requests_hide(tree, decoder_name=None):
    try:
        dec = decoder_name or _PYTI_URL_DECODER_CURRENT
        tree = RequestsHideTransformer(decoder_name=dec).visit(tree)
        ast.fix_missing_locations(tree)
    except Exception:
        pass
    return tree


def meo(code: str):
    tree = ast.parse(code)
    tree = cv().visit(tree)
    tree = pro().visit(tree)
    ast.fix_missing_locations(tree)
    return ast.unparse(tree)
def _runmain(code):
    code = meo(obflzmain(code))
    return code
def _runexec(code):
    code = meo(obflzexec(code))
    return code
def _runimport(code):
    code = meo(obflzimport(code))
    return code

def phienbantrycath(code):
    if sys.version_info < (3, 10):
        tree = trycatch(code.body, 1)
    else:
        tree = trycatch1(code.body, 1)
    mamoi = ast.Module(body=tree, type_ignores=[])
    ast.fix_missing_locations(mamoi)
    return mamoi
def longjunk(code):
    code = junk1().visit(code)
    return code 
def reversing(code):
    return code
def reversing1(code):
    return code

class Cleanstring(__import__('ast').NodeTransformer):
    def __init__(__khangcoderbadao__):
        __khangcoderbadao__.__imports__={}

    def d(__khangcoderbadao__,__khangcoder__):
        __khangcoderbadao__.generic_visit(__khangcoder__)
        if hasattr(__khangcoder__,'body')and isinstance(__khangcoder__.body,list):
            __khangcoder__.body=[s for s in __khangcoder__.body if s is not None]
        return __khangcoder__

    def vs(__khangcoderbadao__,__khangcoder__):
        __khangcoder__=__khangcoderbadao__.d(__khangcoder__)
        if __khangcoder__.body and isinstance(__khangcoder__.body[0],__import__('ast').Expr)and isinstance(__khangcoder__.body[0].value,__import__('ast').Constant)and isinstance(__khangcoder__.body[0].value.value,str):__khangcoder__.body.pop(0)
        return __khangcoder__

    def func(__khangcoderbadao__,__khangcoder__):
        __khangcoder__=__khangcoderbadao__.d(__khangcoder__)
        if __khangcoder__.body and isinstance(__khangcoder__.body[0],__import__('ast').Expr)and isinstance(__khangcoder__.body[0].value,__import__('ast').Constant)and isinstance(__khangcoder__.body[0].value.value,str):__khangcoder__.body.pop(0)
        return __khangcoder__

    def balamon(__khangcoderbadao__,__khangcoder__):
        return __khangcoderbadao__.func(__khangcoder__)

    def idk(__khangcoderbadao__,__khangcoder__):
        __khangcoder__=__khangcoderbadao__.d(__khangcoder__)
        if __khangcoder__.body and isinstance(__khangcoder__.body[0],__import__('ast').Expr)and isinstance(__khangcoder__.body[0].value,__import__('ast').Constant)and isinstance(__khangcoder__.body[0].value.value,str):__khangcoder__.body.pop(0)
        return __khangcoder__

    def visit_Expr(__khangcoderbadao__,__khangcoder__):
        if isinstance(__khangcoder__.value,__import__('ast').Constant)and isinstance(__khangcoder__.value.value,str):return None
        return __khangcoder__

    def visit_Import(__khangcoderbadao__,__khangcoder__):
        for __x__ in __khangcoder__.names:
            __khangcoderbadao__.__imports__[__x__.name]=__x__
        return None

    def visit_Module(__khangcoderbadao__,__khangcoder__):
        __khangcoder__=__khangcoderbadao__.d(__khangcoder__)
        __body__=[]
        if __khangcoderbadao__.__imports__:
            __body__.append(__import__('ast').Import(names=list(__khangcoderbadao__.__imports__.values())))
        __body__+=__khangcoder__.body
        __khangcoder__.body=__body__
        return __khangcoder__

def clean(code):
    tree = ast.parse(code)
    tree = Cleanstring().visit(tree)
    ast.fix_missing_locations(tree)
    return ast.unparse(tree)

def dequybadao(dump, depth=1):
    # FIX BUG #17: cap depth to 1 (no exponential blowup), cache, size guard.
    try:
        depth = int(depth or 1)
    except Exception:
        depth = 1
    if depth != 1:
        depth = 1
    dump = poison_code_object(dump)
    _raw_payload = marshal.dumps(dump)
    import lzma as _lz_ib
    payload = _lz_ib.compress(_raw_payload, preset=6)
    try:
        _cache_key = _pyti_sha256(payload)
        if _cache_key in _DEQUY_CACHE:
            return _DEQUY_CACHE[_cache_key]
    except Exception:
        _cache_key = None
    if len(payload) > 50 * 1024 * 1024:
        raise MemoryError('payload too large')
    # FIX BUG #18: integrity digest of inner payload (verified at runtime).
    _digest = _pyti_sha256(payload)
    for _ in range(depth):
        # FIX BUG #2: 32B key + 8B salt + SHA256-CTR keystream (not 4B repeating XOR).
        # Key/salt/xored are fragmented (no single literal) to block 1-liner extraction.
        import hashlib as _hl_ib, secrets as _sec_ib, base64 as _b64_ib
        key = _sec_ib.token_bytes(32)
        salt = _sec_ib.token_bytes(8)
        _ks = b''.join(_hl_ib.sha256(key + salt + c.to_bytes(4, 'big')).digest() for c in range((len(payload) + 31) // 32))[:len(payload)]
        xored = bytes(b ^ _ks[i] for i, b in enumerate(payload))
        mathuat = '__XxAbyssProxX__'
        # Fragment sensitive literals so no single b'...' blob exists (fix BUG #1/#2).
        _key_expr = _pyti_frag_bytes_expr(key, 16)
        _salt_expr = _pyti_frag_bytes_expr(salt, 8)
        _xor_expr = _pyti_frag_bytes_expr(xored, 256)
        _dg1, _dg2 = _digest[:32], _digest[32:]
        # Hide bad-keyword lists as b64 blobs (anti-grep, fix BUG #7/#8).
        _kw_raw = ','.join(['pycdc', 'decompyle', 'uncompyle', 'decompile', 'deobf', 'disassembl', 'pydisasm', 'unpyc', 'pyfluff', 'marshal_dump', 'tracer', 'hook_exec', 'hook_marshal', 'pylingual', 'pyarmor'])
        _pr_raw = ','.join(['pycdc', 'pycdc.exe', 'decompyle++', 'uncompyle6', 'decompyle', 'pydecomp', 'pylingual', 'xdis', 'pyarmor', 'pyfluff', 'decompile', 'unpyc', 'dis', 'pycdc_gui', 'ida.exe', 'ida64.exe', 'idag.exe', 'idaw.exe', 'x64dbg.exe', 'x32dbg.exe', 'x96dbg.exe', 'cheatengine.exe', 'scylla.exe', 'processhacker.exe', 'procmon.exe', 'wireshark.exe', 'fiddler.exe', 'charles.exe', 'httpcanary.exe', 'mitmproxy.exe', 'burpsuite.exe', 'dnspy.exe', 'de4dot.exe'])
        _kw_b64 = _b64_ib.b64encode(_kw_raw.encode()).decode()
        _pr_b64 = _b64_ib.b64encode(_pr_raw.encode()).decode()
        src = f"""thucheck = __import__('os').path.abspath(__file__)
def TrumXamLol():
    # FIX BUG #11: non-destructive tamper response (no file overwrite).
    try:
        import sys as _s, os as _o
        try:
            _o._exit(95)
        except Exception:
            _s.exit(95)
    except SystemExit: raise
    except Exception:
        raise SystemExit('tamper-detected')
def anti():
    import sys, os, time
    import base64 as _b64a
    _bad_kw = tuple(_b64a.b64decode({_kw_b64!r}).decode().split(','))
    _bad_procs = tuple(_b64a.b64decode({_pr_b64!r}).decode().split(','))
    while True:
        try:
            if sys.gettrace() is not None: TrumXamLol()
            for frame in sys._current_frames().values():
                cf = frame
                while cf:
                    ___khangcoder___{q}____ = (getattr(cf.f_code, 'co_filename', '') or '').lower()
                    ___fn_name___ = (getattr(cf.f_code, 'co_name', '') or '').lower()
                    if any(x in ___khangcoder___{q}____ or x in ___fn_name___ for x in _bad_kw):
                        TrumXamLol()
                        os._exit(97)
                    cf = cf.f_back
            for m in list(sys.modules.keys()):
                if any(x in m.lower() for x in ('pycdc', 'decompyle', 'uncompyle', 'decompile', 'xdis', 'pydisasm', 'pylingual', 'deobfuscator')):
                    TrumXamLol()
                    os._exit(96)
            try:
                import ctypes
                _windll2 = getattr(ctypes, 'windll', None)
                k32 = getattr(_windll2, 'kernel32', None) if _windll2 is not None else None
                if k32:
                    class PROCESSENTRY32W(ctypes.Structure):
                        _fields_ = [('dwSize', ctypes.c_ulong), ('cntUsage', ctypes.c_ulong), ('th32ProcessID', ctypes.c_ulong), ('th32DefaultHeapID', ctypes.c_size_t), ('th32ModuleID', ctypes.c_ulong), ('cntThreads', ctypes.c_ulong), ('th32ParentProcessID', ctypes.c_ulong), ('pcPriClassBase', ctypes.c_long), ('dwFlags', ctypes.c_ulong), ('szExeFile', ctypes.c_wchar * 260)]
                    hSnap = k32.CreateToolhelp32Snapshot(0x00000002, 0)
                    if hSnap != -1:
                        pe = PROCESSENTRY32W()
                        pe.dwSize = ctypes.sizeof(PROCESSENTRY32W)
                        if k32.Process32FirstW(hSnap, ctypes.byref(pe)):
                            while True:
                                if any(x in pe.szExeFile.lower() for x in _bad_procs):
                                    hProc = k32.OpenProcess(0x0001, False, pe.th32ProcessID)
                                    if hProc:
                                        k32.TerminateProcess(hProc, 1)
                                        k32.CloseHandle(hProc)
                                    TrumXamLol()
                                    os._exit(137)
                                if not k32.Process32NextW(hSnap, ctypes.byref(pe)): break
                        k32.CloseHandle(hSnap)
            except Exception: pass
        except: pass
        time.sleep(1.2)
try:
    if '__pyti_dequy_started__' not in globals():
        globals()['__pyti_dequy_started__'] = True
        try:
            import _thread as _th_dequy
            _th_dequy.start_new_thread(anti, ())
        except Exception:
            __import__('threading').Thread(target=anti, daemon=True).start()
except: pass
def __xx0Abyss0xx__():
    # SHA256-CTR keystream + fragmented key/salt/blob + sha256 integrity (fix BUG #2/#18).
    # No single key literal: key/salt/xored are b"".join([...]) fragments.
    __K = ({_key_expr})
    __S = ({_salt_expr})
    __X = ({_xor_expr})
    __D = ({_dg1!r}+{_dg2!r})
    __HL = KhangCoder({enc('hashlib')})
    __N = len(__X)
    __KS = b''.join(__HL.sha256(__K+__S+__c.to_bytes(4, 'big')).digest() for __c in range((__N+32-1)//32))[:__N]
    __P = bytes(__b ^ __KS[__i] for __i, __b in eval({enc('_0x4')})(__X))
    assert __HL.sha256(__P).hexdigest()==__D, 'integrity'
    __LZ = KhangCoder({enc('lzma')})
    __raw_P = __LZ.decompress(__P)
    globals()[{enc(mathuat)}] = JackĐẻCon(__raw_P)
    del __KS, __X, __K, __S, __P
    _m_ld = KhangCoder({enc('marshal')}).loads
    if getattr(_m_ld, '__code__', None) is not None or 'builtin' not in str(type(_m_ld)):
        TrumXamLol()
    return _m_ld({mathuat}), __D, __KhangCoder__({enc('32')}), getattr(KhangCoder({enc("sysconfig")}), {enc("get_path")})({enc("stdlib")})
getattr(KhangCoder({enc('builtins')}), {enc('BotㅤPyTiㅤAbi')})(__xx0Abyss0xx__()[No1], globals(), globals())\n"""
        fname = f'<__PyTiㅤ{random.randint(1000, 9999)}ㅤAbi__>'
        try:
            code = _compile_secure(src, fname, 'exec')
        except Exception:
            code = compile(src, fname, 'exec')
        code = poison_code_object(code)
    # cache single-depth result (fix BUG #17 DoS)
    try:
        _res = marshal.dumps(code)
        if _cache_key is not None:
            _DEQUY_CACHE[_cache_key] = _res
        return _res
    except Exception:
        return marshal.dumps(code)



# ==================== PYTI HYPER-VM ENGINE V4.0 ULTRA BOOSTED ====================
BINARY_OPS = {
    ast.Add: '+',
    ast.Sub: '-',
    ast.Mult: '*',
    ast.Div: '/',
    ast.FloorDiv: '//',
    ast.Mod: '%',
    ast.Pow: '**',
    ast.LShift: '<<',
    ast.RShift: '>>',
    ast.BitOr: '|',
    ast.BitXor: '^',
    ast.BitAnd: '&',
    ast.MatMult: '@',
}

UNARY_OPS = {
    ast.UAdd: '+',
    ast.USub: '-',
    ast.Not: 'not',
    ast.Invert: '~',
}

COMPARE_OPS = {
    ast.Eq: '==',
    ast.NotEq: '!=',
    ast.Lt: '<',
    ast.LtE: '<=',
    ast.Gt: '>',
    ast.GtE: '>=',
    ast.Is: 'is',
    ast.IsNot: 'is not',
    ast.In: 'in',
    ast.NotIn: 'not in',
}

OPCODE_NAMES = [
    'NOP',
    'LOAD_CONST',
    'LOAD_NAME',
    'STORE_NAME',
    'DELETE_NAME',
    'LOAD_GLOBAL',
    'STORE_GLOBAL',
    'DELETE_GLOBAL',
    'LOAD_ATTR',
    'STORE_ATTR',
    'DELETE_ATTR',
    'LOAD_SUBSCR',
    'STORE_SUBSCR',
    'DELETE_SUBSCR',
    'BUILD_LIST',
    'BUILD_TUPLE',
    'BUILD_SET',
    'BUILD_MAP',
    'BUILD_SLICE',
    'BUILD_STRING',
    'LIST_APPEND',
    'SET_ADD',
    'MAP_ADD',
    'BINARY_OP',
    'UNARY_OP',
    'COMPARE_OP',
    'JUMP',
    'JUMP_IF_TRUE',
    'JUMP_IF_FALSE',
    'POP_JUMP_IF_TRUE',
    'POP_JUMP_IF_FALSE',
    'POP_TOP',
    'DUP_TOP',
    'DUP_TOP_TWO',
    'ROT_TWO',
    'ROT_THREE',
    'CALL_FUNC',
    'CALL_KW',
    'CALL_EX',
    'RETURN_VALUE',
    'YIELD_VALUE',
    'GET_ITER',
    'FOR_ITER',
    'IMPORT_NAME',
    'IMPORT_FROM',
    'IMPORT_STAR',
    'SETUP_EXCEPT',
    'POP_EXCEPT',
    'SETUP_WITH',
    'EXIT_WITH',
    'RAISE_VARARGS',
    'MAKE_FUNCTION',
    'MAKE_CLASS',
    'UNPACK_SEQUENCE',
    'FORMAT_VALUE',
    'VM_CHECK',
    'GET_AWAITABLE',
    'GET_AITER',
    'FOR_AITER',
    'SETUP_ASYNC_WITH',
    'EXIT_ASYNC_WITH',
    'STORE_NONLOCAL',
    'DELETE_NONLOCAL',
    'LIST_EXTEND',
    'MAP_UPDATE',
    'SET_UPDATE'
]


class PyTiBoostedVMCompiler:
    def __init__(self, opcode_map=None, seed=None, is_module=True, is_class=False):
        self.constants = []
        self.names = []
        self.instructions = []
        self.loop_stack = []
        self.with_stack = []
        self.label_counter = 0
        self.seed = seed if seed is not None else random.randint(0x10000000, 0x7FFFFFFF)
        self.opcode_map = opcode_map or {name: i for i, name in enumerate(OPCODE_NAMES)}
        self.is_module = is_module
        self.is_class = is_class
        self.globals = set()
        self.nonlocals = set()

    def _collect_scope_decls(self, stmts):
        globs, nonlocs = set(), set()
        for stmt in stmts:
            if isinstance(stmt, ast.Global):
                globs.update(stmt.names)
            elif isinstance(stmt, ast.Nonlocal):
                nonlocs.update(stmt.names)
            elif isinstance(stmt, (ast.If, ast.While, ast.For, ast.AsyncFor, ast.With, ast.AsyncWith)):
                g, n = self._collect_scope_decls(stmt.body)
                globs.update(g); nonlocs.update(n)
                g, n = self._collect_scope_decls(getattr(stmt, 'orelse', []))
                globs.update(g); nonlocs.update(n)
            elif isinstance(stmt, ast.Try):
                g, n = self._collect_scope_decls(stmt.body)
                globs.update(g); nonlocs.update(n)
                for h in stmt.handlers:
                    g, n = self._collect_scope_decls(h.body)
                    globs.update(g); nonlocs.update(n)
                g, n = self._collect_scope_decls(stmt.orelse)
                globs.update(g); nonlocs.update(n)
                g, n = self._collect_scope_decls(stmt.finalbody)
                globs.update(g); nonlocs.update(n)
        return globs, nonlocs

    def new_label(self):
        self.label_counter += 1
        return f"__L_{self.label_counter}"

    def get_const_idx(self, val):
        for idx, c in enumerate(self.constants):
            if type(c) is type(val) and c == val:
                return idx
        self.constants.append(val)
        return len(self.constants) - 1

    def get_name_idx(self, name):
        if name in self.names:
            return self.names.index(name)
        self.names.append(name)
        return len(self.names) - 1

    def emit(self, op, arg=0):
        self.instructions.append((op, arg))

    def emit_label(self, label):
        self.instructions.append(('LABEL', label))

    def compile(self, node):
        if isinstance(node, str):
            node = ast.parse(node)
        if hasattr(node, 'body') and isinstance(node.body, list):
            self.globals, self.nonlocals = self._collect_scope_decls(node.body)
        self.visit(node)
        self.emit('LOAD_CONST', self.get_const_idx(None))
        self.emit('RETURN_VALUE', 0)
        return self.link()

    def link(self):
        label_map = {}
        clean_ins = []
        for op, arg in self.instructions:
            if op == 'LABEL':
                label_map[arg] = len(clean_ins)
            else:
                clean_ins.append((op, arg))
        
        final_ins = []
        for op, arg in clean_ins:
            op_code = self.opcode_map[op]
            if isinstance(arg, str) and arg.startswith('__L_'):
                final_ins.append((op_code, label_map[arg]))
            else:
                final_ins.append((op_code, arg))

        packed_bytes = bytearray()
        seed = self.seed
        num_opcodes = len(OPCODE_NAMES)
        
        pepper = _PYTI_HVM_PEPPER
        epoch = max(1, int(_PYTI_HVM_EPOCH))
        k_mul = _PYTI_HVM_K
        k_add = _PYTI_HVM_K2
        last_e = None
        block = b''
        for idx, (op_code, arg_val) in enumerate(final_ins):
            # Ultra Real VM: SHA256 epoch material + unique per-instruction keys.
            # Key schedule rotates every `epoch` ops — no single static multiplier.
            e = idx // epoch
            if e != last_e:
                block = _pyti_hvm_epoch_block(seed, e, pepper, k_mul, k_add)
                last_e = e
            k_op, k_arg = _pyti_hvm_ins_keys(block, idx, num_opcodes)
            enc_op = (op_code + k_op) % num_opcodes
            enc_arg = (int(arg_val) ^ k_arg) & 0xFFFFFFFF
            packed_bytes.extend(struct.pack('>BI', enc_op, enc_arg))

        chk = zlib.adler32(packed_bytes) & 0xFFFFFFFF

        return {
            'bytecode': bytes(packed_bytes),
            'length': len(final_ins),
            'seed': self.seed,
            'chk': chk,
            'constants': self.constants,
            'names': self.names,
            'opcode_map': self.opcode_map
        }

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise NotImplementedError(f"BoostedVM AST Visitor not implemented for {node.__class__.__name__}")

    def visit_Module(self, node):
        for stmt in node.body:
            self.visit(stmt)

    def visit_Expr(self, node):
        self.visit(node.value)
        self.emit('POP_TOP', 0)

    def visit_Pass(self, node):
        self.emit('NOP', 0)

    def visit_Constant(self, node):
        idx = self.get_const_idx(node.value)
        self.emit('LOAD_CONST', idx)

    def visit_Name(self, node):
        idx = self.get_name_idx(node.id)
        if isinstance(node.ctx, ast.Load):
            if node.id in self.globals:
                self.emit('LOAD_GLOBAL', idx)
            else:
                self.emit('LOAD_NAME', idx)
        elif isinstance(node.ctx, ast.Store):
            if node.id in self.globals:
                self.emit('STORE_GLOBAL', idx)
            elif node.id in self.nonlocals:
                self.emit('STORE_NONLOCAL', idx)
            else:
                self.emit('STORE_NAME', idx)
        elif isinstance(node.ctx, ast.Del):
            if node.id in self.globals:
                self.emit('DELETE_GLOBAL', idx)
            elif node.id in self.nonlocals:
                self.emit('DELETE_NONLOCAL', idx)
            else:
                self.emit('DELETE_NAME', idx)

    def visit_Global(self, node):
        pass

    def visit_Nonlocal(self, node):
        pass

    def visit_Assign(self, node):
        self.visit(node.value)
        for i, target in enumerate(node.targets):
            if i < len(node.targets) - 1:
                self.emit('DUP_TOP', 0)
            self.visit_target(target)

    def visit_AnnAssign(self, node):
        if self.is_class and isinstance(node.target, ast.Name):
            self.visit(node.annotation)
            self.emit('LOAD_NAME', self.get_name_idx('__annotations__'))
            self.emit('LOAD_CONST', self.get_const_idx(node.target.id))
            self.emit('STORE_SUBSCR', 0)
        if node.value:
            self.visit(node.value)
            self.visit_target(node.target)

    def visit_AugAssign(self, node):
        if isinstance(node.target, ast.Name):
            idx = self.get_name_idx(node.target.id)
            if node.target.id in self.globals:
                self.emit('LOAD_GLOBAL', idx)
                self.visit(node.value)
                op_sym = BINARY_OPS[node.op.__class__]
                self.emit('BINARY_OP', self.get_const_idx(op_sym))
                self.emit('STORE_GLOBAL', idx)
            elif node.target.id in self.nonlocals:
                self.emit('LOAD_NAME', idx)
                self.visit(node.value)
                op_sym = BINARY_OPS[node.op.__class__]
                self.emit('BINARY_OP', self.get_const_idx(op_sym))
                self.emit('STORE_NONLOCAL', idx)
            else:
                self.emit('LOAD_NAME', idx)
                self.visit(node.value)
                op_sym = BINARY_OPS[node.op.__class__]
                self.emit('BINARY_OP', self.get_const_idx(op_sym))
                self.emit('STORE_NAME', idx)
        elif isinstance(node.target, ast.Attribute):
            self.visit(node.target.value)
            self.emit('DUP_TOP', 0)
            attr_idx = self.get_name_idx(node.target.attr)
            self.emit('LOAD_ATTR', attr_idx)
            self.visit(node.value)
            op_sym = BINARY_OPS[node.op.__class__]
            self.emit('BINARY_OP', self.get_const_idx(op_sym))
            self.emit('ROT_TWO', 0)
            self.emit('STORE_ATTR', attr_idx)
        elif isinstance(node.target, ast.Subscript):
            self.visit(node.target.value)
            self.visit(node.target.slice)
            self.emit('DUP_TOP_TWO', 0)
            self.emit('LOAD_SUBSCR', 0)
            self.visit(node.value)
            op_sym = BINARY_OPS[node.op.__class__]
            self.emit('BINARY_OP', self.get_const_idx(op_sym))
            self.emit('ROT_THREE', 0)
            self.emit('STORE_SUBSCR', 0)
        else:
            raise NotImplementedError(f"AugAssign not supported for {type(node.target)}")

    def visit_target(self, target):
        if isinstance(target, ast.Name):
            idx = self.get_name_idx(target.id)
            if target.id in self.globals:
                self.emit('STORE_GLOBAL', idx)
            elif target.id in self.nonlocals:
                self.emit('STORE_NONLOCAL', idx)
            else:
                self.emit('STORE_NAME', idx)
        elif isinstance(target, ast.Attribute):
            self.visit(target.value)
            self.emit('STORE_ATTR', self.get_name_idx(target.attr))
        elif isinstance(target, ast.Subscript):
            self.visit(target.value)
            self.visit(target.slice)
            self.emit('STORE_SUBSCR', 0)
        elif isinstance(target, (ast.Tuple, ast.List)):
            self.emit('UNPACK_SEQUENCE', len(target.elts))
            for elt in target.elts:
                self.visit_target(elt)
        else:
            raise NotImplementedError(f"Target not supported {type(target)}")

    def visit_Delete(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                idx = self.get_name_idx(target.id)
                if target.id in self.globals:
                    self.emit('DELETE_GLOBAL', idx)
                elif target.id in self.nonlocals:
                    self.emit('DELETE_NONLOCAL', idx)
                else:
                    self.emit('DELETE_NAME', idx)
            elif isinstance(target, ast.Attribute):
                self.visit(target.value)
                self.emit('DELETE_ATTR', self.get_name_idx(target.attr))
            elif isinstance(target, ast.Subscript):
                self.visit(target.value)
                self.visit(target.slice)
                self.emit('DELETE_SUBSCR', 0)

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)
        op_sym = BINARY_OPS[node.op.__class__]
        self.emit('BINARY_OP', self.get_const_idx(op_sym))

    def visit_UnaryOp(self, node):
        self.visit(node.operand)
        op_sym = UNARY_OPS[node.op.__class__]
        self.emit('UNARY_OP', self.get_const_idx(op_sym))

    def visit_BoolOp(self, node):
        is_and = isinstance(node.op, ast.And)
        end_label = self.new_label()
        for i, val in enumerate(node.values):
            self.visit(val)
            if i < len(node.values) - 1:
                self.emit('DUP_TOP', 0)
                if is_and:
                    self.emit('POP_JUMP_IF_FALSE', end_label)
                else:
                    self.emit('POP_JUMP_IF_TRUE', end_label)
        self.emit_label(end_label)

    def visit_Compare(self, node):
        if len(node.ops) == 1:
            self.visit(node.left)
            self.visit(node.comparators[0])
            op_sym = COMPARE_OPS[node.ops[0].__class__]
            self.emit('COMPARE_OP', self.get_const_idx(op_sym))
        else:
            end_label = self.new_label()
            self.visit(node.left)
            for i, (op, comp) in enumerate(zip(node.ops, node.comparators)):
                self.visit(comp)
                if i < len(node.ops) - 1:
                    self.emit('DUP_TOP', 0)
                    self.emit('ROT_TWO', 0)
                op_sym = COMPARE_OPS[op.__class__]
                self.emit('COMPARE_OP', self.get_const_idx(op_sym))
                if i < len(node.ops) - 1:
                    self.emit('DUP_TOP', 0)
                    self.emit('POP_JUMP_IF_FALSE', end_label)
                    self.emit('ROT_TWO', 0)
            self.emit_label(end_label)

    def visit_Call(self, node):
        has_star_args = any(isinstance(a, ast.Starred) for a in node.args)
        has_star_kwargs = any(kw.arg is None for kw in node.keywords)

        if has_star_args or has_star_kwargs:
            self.visit(node.func)
            self.emit('BUILD_LIST', 0)
            for arg in node.args:
                if isinstance(arg, ast.Starred):
                    self.visit(arg.value)
                    self.emit('LIST_EXTEND', 1)
                else:
                    self.visit(arg)
                    self.emit('LIST_APPEND', 1)
            self.emit('BUILD_MAP', 0)
            for kw in node.keywords:
                if kw.arg is None:
                    self.visit(kw.value)
                    self.emit('MAP_UPDATE', 1)
                else:
                    self.emit('LOAD_CONST', self.get_const_idx(kw.arg))
                    self.visit(kw.value)
                    self.emit('MAP_ADD', 1)
            self.emit('CALL_EX', 0)
        elif node.keywords:
            self.visit(node.func)
            for arg in node.args:
                self.visit(arg)
            kw_names = []
            for kw in node.keywords:
                kw_names.append(kw.arg)
                self.visit(kw.value)
            kw_idx = self.get_const_idx(tuple(kw_names))
            self.emit('CALL_KW', (len(node.args) << 16) | (kw_idx & 0xFFFF))
        else:
            self.visit(node.func)
            for arg in node.args:
                self.visit(arg)
            self.emit('CALL_FUNC', len(node.args))

    def visit_Attribute(self, node):
        self.visit(node.value)
        idx = self.get_name_idx(node.attr)
        self.emit('LOAD_ATTR', idx)

    def visit_Subscript(self, node):
        self.visit(node.value)
        self.visit(node.slice)
        self.emit('LOAD_SUBSCR', 0)

    def visit_Slice(self, node):
        count = 0
        if node.lower:
            self.visit(node.lower)
            count += 1
        else:
            self.emit('LOAD_CONST', self.get_const_idx(None))
            count += 1
        if node.upper:
            self.visit(node.upper)
            count += 1
        else:
            self.emit('LOAD_CONST', self.get_const_idx(None))
            count += 1
        if node.step:
            self.visit(node.step)
            count += 1
        else:
            self.emit('LOAD_CONST', self.get_const_idx(None))
            count += 1
        self.emit('BUILD_SLICE', count)

    def visit_List(self, node):
        has_unpack = any(isinstance(e, ast.Starred) for e in node.elts)
        if has_unpack:
            self.emit('BUILD_LIST', 0)
            for elt in node.elts:
                if isinstance(elt, ast.Starred):
                    self.visit(elt.value)
                    self.emit('LIST_EXTEND', 1)
                else:
                    self.visit(elt)
                    self.emit('LIST_APPEND', 1)
        else:
            for elt in node.elts:
                self.visit(elt)
            self.emit('BUILD_LIST', len(node.elts))

    def visit_Tuple(self, node):
        has_unpack = any(isinstance(e, ast.Starred) for e in node.elts)
        if has_unpack:
            self.emit('BUILD_LIST', 0)
            for elt in node.elts:
                if isinstance(elt, ast.Starred):
                    self.visit(elt.value)
                    self.emit('LIST_EXTEND', 1)
                else:
                    self.visit(elt)
                    self.emit('LIST_APPEND', 1)
            self.emit('LOAD_NAME', self.get_name_idx('tuple'))
            self.emit('ROT_TWO', 0)
            self.emit('CALL_FUNC', 1)
        else:
            for elt in node.elts:
                self.visit(elt)
            self.emit('BUILD_TUPLE', len(node.elts))

    def visit_Set(self, node):
        has_unpack = any(isinstance(e, ast.Starred) for e in node.elts)
        if has_unpack:
            self.emit('BUILD_SET', 0)
            for elt in node.elts:
                if isinstance(elt, ast.Starred):
                    self.visit(elt.value)
                    self.emit('SET_UPDATE', 1)
                else:
                    self.visit(elt)
                    self.emit('SET_ADD', 1)
        else:
            for elt in node.elts:
                self.visit(elt)
            self.emit('BUILD_SET', len(node.elts))

    def visit_Dict(self, node):
        has_unpack = any(k is None for k in node.keys)
        if has_unpack:
            self.emit('BUILD_MAP', 0)
            for k, v in zip(node.keys, node.values):
                if k is None:
                    self.visit(v)
                    self.emit('MAP_UPDATE', 1)
                else:
                    self.emit('LOAD_CONST', self.get_const_idx(k.value) if isinstance(k, ast.Constant) else None)
                    if not isinstance(k, ast.Constant):
                        self.instructions.pop()
                        self.visit(k)
                    self.visit(v)
                    self.emit('MAP_ADD', 1)
        else:
            for k, v in zip(node.keys, node.values):
                self.visit(k)
                self.visit(v)
            self.emit('BUILD_MAP', len(node.keys))

    def visit_JoinedStr(self, node):
        for val in node.values:
            self.visit(val)
        self.emit('BUILD_STRING', len(node.values))

    def visit_FormattedValue(self, node):
        self.visit(node.value)
        fmt = node.format_spec.values[0].value if (node.format_spec and node.format_spec.values) else ''
        self.emit('FORMAT_VALUE', self.get_const_idx((node.conversion, fmt)))

    def visit_NamedExpr(self, node):
        self.visit(node.value)
        self.emit('DUP_TOP', 0)
        self.visit_target(node.target)

    def visit_Starred(self, node):
        self.visit(node.value)

    def visit_Yield(self, node):
        if node.value:
            self.visit(node.value)
        else:
            self.emit('LOAD_CONST', self.get_const_idx(None))
        self.emit('YIELD_VALUE', 0)

    def visit_Await(self, node):
        self.visit(node.value)
        self.emit('GET_AWAITABLE', 0)

    def visit_GeneratorExp(self, node):
        self.emit('BUILD_LIST', 0)
        self._compile_list_comprehension(node.generators, 0, node.elt, depth=1)
        self.emit('GET_ITER', 0)

    def visit_If(self, node):
        else_label = self.new_label()
        end_label = self.new_label()
        self.visit(node.test)
        self.emit('POP_JUMP_IF_FALSE', else_label)
        for stmt in node.body:
            self.visit(stmt)
        self.emit('JUMP', end_label)
        self.emit_label(else_label)
        if node.orelse:
            for stmt in node.orelse:
                self.visit(stmt)
        self.emit_label(end_label)

    def visit_IfExp(self, node):
        else_label = self.new_label()
        end_label = self.new_label()
        self.visit(node.test)
        self.emit('POP_JUMP_IF_FALSE', else_label)
        self.visit(node.body)
        self.emit('JUMP', end_label)
        self.emit_label(else_label)
        self.visit(node.orelse)
        self.emit_label(end_label)

    def visit_While(self, node):
        loop_start = self.new_label()
        exhaust_label = self.new_label()
        end_label = self.new_label()
        self.loop_stack.append((end_label, loop_start, len(self.with_stack), False))
        self.emit_label(loop_start)
        self.visit(node.test)
        self.emit('POP_JUMP_IF_FALSE', exhaust_label)
        for stmt in node.body:
            self.visit(stmt)
        self.emit('JUMP', loop_start)
        self.emit_label(exhaust_label)
        if node.orelse:
            for stmt in node.orelse:
                self.visit(stmt)
        self.emit_label(end_label)
        self.loop_stack.pop()

    def visit_For(self, node):
        loop_start = self.new_label()
        exhaust_label = self.new_label()
        end_label = self.new_label()
        self.loop_stack.append((end_label, loop_start, len(self.with_stack), True))
        self.visit(node.iter)
        self.emit('GET_ITER', 0)
        self.emit_label(loop_start)
        self.emit('FOR_ITER', exhaust_label)
        self.visit_target(node.target)
        for stmt in node.body:
            self.visit(stmt)
        self.emit('JUMP', loop_start)
        self.emit_label(exhaust_label)
        if node.orelse:
            for stmt in node.orelse:
                self.visit(stmt)
        self.emit_label(end_label)
        self.loop_stack.pop()

    def visit_AsyncFor(self, node):
        loop_start = self.new_label()
        exhaust_label = self.new_label()
        end_label = self.new_label()
        self.loop_stack.append((end_label, loop_start, len(self.with_stack), True))
        self.visit(node.iter)
        self.emit('GET_AITER', 0)
        self.emit_label(loop_start)
        self.emit('FOR_AITER', exhaust_label)
        self.visit_target(node.target)
        for stmt in node.body:
            self.visit(stmt)
        self.emit('JUMP', loop_start)
        self.emit_label(exhaust_label)
        if node.orelse:
            for stmt in node.orelse:
                self.visit(stmt)
        self.emit_label(end_label)
        self.loop_stack.pop()

    def visit_Break(self, node):
        if self.loop_stack:
            break_label, _, with_depth, is_for_iter = self.loop_stack[-1]
            for is_async in reversed(self.with_stack[with_depth:]):
                if is_async:
                    self.emit('EXIT_ASYNC_WITH', 0)
                else:
                    self.emit('EXIT_WITH', 0)
            if is_for_iter:
                self.emit('POP_TOP', 0)
            self.emit('JUMP', break_label)

    def visit_Continue(self, node):
        if self.loop_stack:
            _, continue_label, with_depth, _ = self.loop_stack[-1]
            for is_async in reversed(self.with_stack[with_depth:]):
                if is_async:
                    self.emit('EXIT_ASYNC_WITH', 0)
                else:
                    self.emit('EXIT_WITH', 0)
            self.emit('JUMP', continue_label)

    def visit_Return(self, node):
        if node.value:
            self.visit(node.value)
        else:
            self.emit('LOAD_CONST', self.get_const_idx(None))
        self.emit('RETURN_VALUE', 0)

    def visit_Import(self, node):
        for alias in node.names:
            self.emit('LOAD_CONST', self.get_const_idx(0))
            self.emit('LOAD_CONST', self.get_const_idx(None))
            self.emit('IMPORT_NAME', self.get_name_idx(alias.name))
            if alias.asname:
                parts = alias.name.split('.')
                for p in parts[1:]:
                    self.emit('LOAD_ATTR', self.get_name_idx(p))
                self.emit('STORE_NAME', self.get_name_idx(alias.asname))
            else:
                top_pkg = alias.name.split('.')[0]
                self.emit('STORE_NAME', self.get_name_idx(top_pkg))

    def visit_ImportFrom(self, node):
        mod_name = node.module or ''
        from_list = tuple(alias.name for alias in node.names)
        self.emit('LOAD_CONST', self.get_const_idx(node.level))
        self.emit('LOAD_CONST', self.get_const_idx(from_list))
        self.emit('IMPORT_NAME', self.get_name_idx(mod_name))
        for alias in node.names:
            if alias.name == '*':
                self.emit('IMPORT_STAR', 0)
            else:
                self.emit('IMPORT_FROM', self.get_name_idx(alias.name))
                store_as = alias.asname or alias.name
                self.emit('STORE_NAME', self.get_name_idx(store_as))
        self.emit('POP_TOP', 0)

    def visit_Try(self, node):
        if node.finalbody:
            finally_except = self.new_label()
            finally_normal = self.new_label()
            self.emit('SETUP_EXCEPT', finally_except)

            if node.handlers:
                inner_except = self.new_label()
                inner_end = self.new_label()
                self.emit('SETUP_EXCEPT', inner_except)
                for stmt in node.body:
                    self.visit(stmt)
                self.emit('POP_EXCEPT', 0)
                if node.orelse:
                    for stmt in node.orelse:
                        self.visit(stmt)
                self.emit('JUMP', inner_end)

                self.emit_label(inner_except)
                for handler in node.handlers:
                    next_h = self.new_label()
                    if handler.type:
                        self.emit('DUP_TOP', 0)
                        self.visit(handler.type)
                        self.emit('COMPARE_OP', self.get_const_idx('exception_match'))
                        self.emit('POP_JUMP_IF_FALSE', next_h)
                    if handler.name:
                        if handler.name in self.globals:
                            self.emit('STORE_GLOBAL', self.get_name_idx(handler.name))
                        elif handler.name in self.nonlocals:
                            self.emit('STORE_NONLOCAL', self.get_name_idx(handler.name))
                        else:
                            self.emit('STORE_NAME', self.get_name_idx(handler.name))
                    else:
                        self.emit('POP_TOP', 0)
                    for stmt in handler.body:
                        self.visit(stmt)
                    self.emit('JUMP', inner_end)
                    self.emit_label(next_h)
                self.emit('RAISE_VARARGS', 1)
                self.emit_label(inner_end)
            else:
                for stmt in node.body:
                    self.visit(stmt)
                if node.orelse:
                    for stmt in node.orelse:
                        self.visit(stmt)

            self.emit('POP_EXCEPT', 0)
            for stmt in node.finalbody:
                self.visit(stmt)
            self.emit('JUMP', finally_normal)

            self.emit_label(finally_except)
            for stmt in node.finalbody:
                self.visit(stmt)
            self.emit('RAISE_VARARGS', 1)
            self.emit_label(finally_normal)
        else:
            except_label = self.new_label()
            end_label = self.new_label()
            self.emit('SETUP_EXCEPT', except_label)
            for stmt in node.body:
                self.visit(stmt)
            self.emit('POP_EXCEPT', 0)
            if node.orelse:
                for stmt in node.orelse:
                    self.visit(stmt)
            self.emit('JUMP', end_label)

            self.emit_label(except_label)
            for handler in node.handlers:
                next_h = self.new_label()
                if handler.type:
                    self.emit('DUP_TOP', 0)
                    self.visit(handler.type)
                    self.emit('COMPARE_OP', self.get_const_idx('exception_match'))
                    self.emit('POP_JUMP_IF_FALSE', next_h)
                if handler.name:
                    if handler.name in self.globals:
                        self.emit('STORE_GLOBAL', self.get_name_idx(handler.name))
                    elif handler.name in self.nonlocals:
                        self.emit('STORE_NONLOCAL', self.get_name_idx(handler.name))
                    else:
                        self.emit('STORE_NAME', self.get_name_idx(handler.name))
                else:
                    self.emit('POP_TOP', 0)
                for stmt in handler.body:
                    self.visit(stmt)
                self.emit('JUMP', end_label)
                self.emit_label(next_h)
            self.emit('RAISE_VARARGS', 1)
            self.emit_label(end_label)

    def visit_With(self, node):
        end_label = self.new_label()
        for item in node.items:
            self.visit(item.context_expr)
            self.emit('SETUP_WITH', end_label)
            self.with_stack.append(False)
            if item.optional_vars:
                self.visit_target(item.optional_vars)
            else:
                self.emit('POP_TOP', 0)
        for stmt in node.body:
            self.visit(stmt)
        for _ in node.items:
            self.emit('EXIT_WITH', 0)
            self.with_stack.pop()
        self.emit_label(end_label)

    def visit_AsyncWith(self, node):
        end_label = self.new_label()
        for item in node.items:
            self.visit(item.context_expr)
            self.emit('SETUP_ASYNC_WITH', end_label)
            self.with_stack.append(True)
            if item.optional_vars:
                self.visit_target(item.optional_vars)
            else:
                self.emit('POP_TOP', 0)
        for stmt in node.body:
            self.visit(stmt)
        for _ in node.items:
            self.emit('EXIT_ASYNC_WITH', 0)
            self.with_stack.pop()
        self.emit_label(end_label)

    def visit_Raise(self, node):
        if node.exc:
            self.visit(node.exc)
            self.emit('RAISE_VARARGS', 1)
        else:
            self.emit('RAISE_VARARGS', 0)

    def visit_Assert(self, node):
        pass_label = self.new_label()
        self.visit(node.test)
        self.emit('POP_JUMP_IF_TRUE', pass_label)
        if node.msg:
            self.visit(node.msg)
            self.emit('LOAD_NAME', self.get_name_idx('AssertionError'))
            self.emit('ROT_TWO', 0)
            self.emit('CALL_FUNC', 1)
        else:
            self.emit('LOAD_NAME', self.get_name_idx('AssertionError'))
            self.emit('CALL_FUNC', 0)
        self.emit('RAISE_VARARGS', 1)
        self.emit_label(pass_label)

    def _compile_func_def(self, node, is_async=False):
        sub_compiler = PyTiBoostedVMCompiler(opcode_map=self.opcode_map, seed=self.seed, is_module=False)
        sub_code = sub_compiler.compile(ast.Module(body=node.body, type_ignores=[]))
        
        posonly_args = [a.arg for a in getattr(node.args, 'posonlyargs', [])]
        pos_args = [a.arg for a in node.args.args]
        all_pos = posonly_args + pos_args
        kwonly_args = [a.arg for a in getattr(node.args, 'kwonlyargs', [])]

        defaults_count = len(node.args.defaults)
        vararg = node.args.vararg.arg if node.args.vararg else None
        kwarg = node.args.kwarg.arg if node.args.kwarg else None

        for d in node.args.defaults:
            self.visit(d)
        self.emit('BUILD_TUPLE', defaults_count)

        kw_defs_count = 0
        for k_arg, k_def in zip(node.args.kwonlyargs, getattr(node.args, 'kw_defaults', [])):
            if k_def is not None:
                self.emit('LOAD_CONST', self.get_const_idx(k_arg.arg))
                self.visit(k_def)
                kw_defs_count += 1
        self.emit('BUILD_MAP', kw_defs_count)

        fn_meta = {
            'name': node.name,
            'pos_args': all_pos,
            'kwonly_args': kwonly_args,
            'vararg': vararg,
            'kwarg': kwarg,
            'sub_code': sub_code,
            'is_async': is_async
        }
        meta_idx = self.get_const_idx(fn_meta)
        self.emit('MAKE_FUNCTION', meta_idx)
        
        if node.decorator_list:
            for dec in reversed(node.decorator_list):
                self.visit(dec)
                self.emit('ROT_TWO', 0)
                self.emit('CALL_FUNC', 1)
        
        idx = self.get_name_idx(node.name)
        if node.name in self.globals:
            self.emit('STORE_GLOBAL', idx)
        elif node.name in self.nonlocals:
            self.emit('STORE_NONLOCAL', idx)
        else:
            self.emit('STORE_NAME', idx)

    def visit_FunctionDef(self, node):
        self._compile_func_def(node, is_async=False)

    def visit_AsyncFunctionDef(self, node):
        self._compile_func_def(node, is_async=True)

    def visit_Lambda(self, node):
        sub_compiler = PyTiBoostedVMCompiler(opcode_map=self.opcode_map, seed=self.seed, is_module=False)
        sub_code = sub_compiler.compile(ast.Return(value=node.body))
        
        posonly_args = [a.arg for a in getattr(node.args, 'posonlyargs', [])]
        pos_args = [a.arg for a in node.args.args]
        all_pos = posonly_args + pos_args
        kwonly_args = [a.arg for a in getattr(node.args, 'kwonlyargs', [])]

        defaults_count = len(node.args.defaults)
        vararg = node.args.vararg.arg if node.args.vararg else None
        kwarg = node.args.kwarg.arg if node.args.kwarg else None

        for d in node.args.defaults:
            self.visit(d)
        self.emit('BUILD_TUPLE', defaults_count)

        kw_defs_count = 0
        for k_arg, k_def in zip(node.args.kwonlyargs, getattr(node.args, 'kw_defaults', [])):
            if k_def is not None:
                self.emit('LOAD_CONST', self.get_const_idx(k_arg.arg))
                self.visit(k_def)
                kw_defs_count += 1
        self.emit('BUILD_MAP', kw_defs_count)

        fn_meta = {
            'name': '<lambda>',
            'pos_args': all_pos,
            'kwonly_args': kwonly_args,
            'vararg': vararg,
            'kwarg': kwarg,
            'sub_code': sub_code,
            'is_async': False
        }
        meta_idx = self.get_const_idx(fn_meta)
        self.emit('MAKE_FUNCTION', meta_idx)

    def visit_ClassDef(self, node):
        sub_compiler = PyTiBoostedVMCompiler(opcode_map=self.opcode_map, seed=self.seed, is_module=False, is_class=True)
        sub_code = sub_compiler.compile(ast.Module(body=node.body, type_ignores=[]))
        
        for base in node.bases:
            self.visit(base)
        self.emit('BUILD_TUPLE', len(node.bases))

        class_meta = {
            'name': node.name,
            'sub_code': sub_code
        }
        meta_idx = self.get_const_idx(class_meta)
        self.emit('MAKE_CLASS', meta_idx)
        
        if node.decorator_list:
            for dec in reversed(node.decorator_list):
                self.visit(dec)
                self.emit('ROT_TWO', 0)
                self.emit('CALL_FUNC', 1)
        
        idx = self.get_name_idx(node.name)
        if node.name in self.globals:
            self.emit('STORE_GLOBAL', idx)
        elif node.name in self.nonlocals:
            self.emit('STORE_NONLOCAL', idx)
        else:
            self.emit('STORE_NAME', idx)

    def visit_ListComp(self, node):
        self.emit('BUILD_LIST', 0)
        self._compile_list_comprehension(node.generators, 0, node.elt, depth=1)

    def visit_SetComp(self, node):
        self.emit('BUILD_SET', 0)
        self._compile_set_comprehension(node.generators, 0, node.elt, depth=1)

    def visit_DictComp(self, node):
        self.emit('BUILD_MAP', 0)
        self._compile_dict_comprehension(node.generators, 0, node.key, node.value, depth=1)

    def _compile_list_comprehension(self, generators, gen_idx, elt, depth):
        if gen_idx >= len(generators):
            self.visit(elt)
            self.emit('LIST_APPEND', depth)
            return

        gen = generators[gen_idx]
        loop_start = self.new_label()
        loop_end = self.new_label()

        self.visit(gen.iter)
        if getattr(gen, 'is_async', 0):
            self.emit('GET_AITER', 0)
            self.emit_label(loop_start)
            self.emit('FOR_AITER', loop_end)
        else:
            self.emit('GET_ITER', 0)
            self.emit_label(loop_start)
            self.emit('FOR_ITER', loop_end)
        self.visit_target(gen.target)

        skip_if = None
        if gen.ifs:
            skip_if = self.new_label()
            for condition in gen.ifs:
                self.visit(condition)
                self.emit('POP_JUMP_IF_FALSE', skip_if)

        self._compile_list_comprehension(generators, gen_idx + 1, elt, depth + 1)

        if skip_if:
            self.emit_label(skip_if)

        self.emit('JUMP', loop_start)
        self.emit_label(loop_end)

    def _compile_set_comprehension(self, generators, gen_idx, elt, depth):
        if gen_idx >= len(generators):
            self.visit(elt)
            self.emit('SET_ADD', depth)
            return

        gen = generators[gen_idx]
        loop_start = self.new_label()
        loop_end = self.new_label()

        self.visit(gen.iter)
        if getattr(gen, 'is_async', 0):
            self.emit('GET_AITER', 0)
            self.emit_label(loop_start)
            self.emit('FOR_AITER', loop_end)
        else:
            self.emit('GET_ITER', 0)
            self.emit_label(loop_start)
            self.emit('FOR_ITER', loop_end)
        self.visit_target(gen.target)

        skip_if = None
        if gen.ifs:
            skip_if = self.new_label()
            for condition in gen.ifs:
                self.visit(condition)
                self.emit('POP_JUMP_IF_FALSE', skip_if)

        self._compile_set_comprehension(generators, gen_idx + 1, elt, depth + 1)

        if skip_if:
            self.emit_label(skip_if)

        self.emit('JUMP', loop_start)
        self.emit_label(loop_end)

    def _compile_dict_comprehension(self, generators, gen_idx, key_node, val_node, depth):
        if gen_idx >= len(generators):
            self.visit(key_node)
            self.visit(val_node)
            self.emit('MAP_ADD', depth)
            return

        gen = generators[gen_idx]
        loop_start = self.new_label()
        loop_end = self.new_label()

        self.visit(gen.iter)
        if getattr(gen, 'is_async', 0):
            self.emit('GET_AITER', 0)
            self.emit_label(loop_start)
            self.emit('FOR_AITER', loop_end)
        else:
            self.emit('GET_ITER', 0)
            self.emit_label(loop_start)
            self.emit('FOR_ITER', loop_end)
        self.visit_target(gen.target)

        skip_if = None
        if gen.ifs:
            skip_if = self.new_label()
            for condition in gen.ifs:
                self.visit(condition)
                self.emit('POP_JUMP_IF_FALSE', skip_if)

        self._compile_dict_comprehension(generators, gen_idx + 1, key_node, val_node, depth + 1)

        if skip_if:
            self.emit_label(skip_if)

        self.emit('JUMP', loop_start)
        self.emit_label(loop_end)


def generate_hyper_vm_runtime():
    common_helpers = r'''
def _bin_calc(l, r, op):
    if op == '+': return l + r
    elif op == '-': return l - r
    elif op == '*': return l * r
    elif op == '/': return l / r
    elif op == '//': return l // r
    elif op == '%': return l % r
    elif op == '**': return l ** r
    elif op == '<<': return l << r
    elif op == '>>': return l >> r
    elif op == '|': return l | r
    elif op == '^': return l ^ r
    elif op == '&': return l & r
    elif op == '@': return l @ r
    raise RuntimeError(f"Unknown binary op: {op}")

def _unary_calc(v, op):
    if op == '+': return +v
    elif op == '-': return -v
    elif op == 'not': return not v
    elif op == '~': return ~v
    raise RuntimeError(f"Unknown unary op: {op}")

def _comp_calc(l, r, op):
    if op == '==': return l == r
    elif op == '!=': return l != r
    elif op == '<': return l < r
    elif op == '<=': return l <= r
    elif op == '>': return l > r
    elif op == '>=': return l >= r
    elif op == 'is': return l is r
    elif op == 'is not': return l is not r
    elif op == 'in': return l in r
    elif op == 'not in': return l not in r
    elif op == 'exception_match':
        if isinstance(r, tuple):
            return isinstance(l, r)
        elif isinstance(r, type) and issubclass(r, BaseException):
            return isinstance(l, r)
        return False
    raise RuntimeError(f"Unknown compare op: {op}")

__HVM_P__ = __HVM_PEP__
__HVM_S__ = __HVM_SALT__

def __HVM_UNWRAP__(__d__):
    _h = __import__(__HVM_HL__)
    out = bytearray(len(__d__))
    pos = 0
    ctr = 0
    while pos < len(__d__):
        blk = _h.sha256(__HVM_P__ + __HVM_S__ + ctr.to_bytes(4, 'big')).digest()
        n = 32 if (len(__d__) - pos) > 32 else (len(__d__) - pos)
        j = 0
        while j < n:
            out[pos + j] = __d__[pos + j] ^ blk[j]
            j += 1
        pos += n
        ctr += 1
    return bytes(out)

def _vm_init(__pkg__):
    import sys, zlib
    __raw_bc__ = __pkg__['bytecode']
    if (zlib.adler32(__raw_bc__) & 0xFFFFFFFF) != __pkg__['chk']:
        try:
            import ctypes; ctypes.memset(0, 0, 1)
        except: pass
        sys.exit(88)
    __bmap__ = __pkg__['opcode_map']
    __rmap__ = {v: k for k, v in __bmap__.items()}
    return {
        'b': __raw_bc__,
        'r': __rmap__,
        'n': __pkg__['length'],
        's': __pkg__['seed'],
        'p': __HVM_P__,
        'e': __HVM_EP__,
        'km': __HVM_KM__,
        'ka': __HVM_KA__,
        'h': __import__(__HVM_HL__),
        'no': len(__rmap__),
        '_e': None,
        '_blk': b'',
    }

def _fetch_ins(__vmx__, __i):
    import struct
    __ep = __vmx__['e']
    __eid = __i // __ep
    if __vmx__['_e'] != __eid:
        __h = __vmx__['h']
        __blk = __h.sha256(
            (__vmx__['s'] & 0xFFFFFFFFFFFFFFFF).to_bytes(8, 'big') +
            (__eid & 0xFFFFFFFF).to_bytes(4, 'big') +
            __vmx__['p'] +
            (__vmx__['km'] & 0xFFFFFFFF).to_bytes(4, 'big') +
            (__vmx__['ka'] & 0xFFFFFFFF).to_bytes(4, 'big')
        ).digest()
        __vmx__['_e'] = __eid
        __vmx__['_blk'] = __blk
    else:
        __blk = __vmx__['_blk']
    __w0 = int.from_bytes(__blk[0:4], 'big')
    __w1 = int.from_bytes(__blk[4:8], 'big')
    __w2 = int.from_bytes(__blk[8:12], 'big')
    __w3 = int.from_bytes(__blk[12:16], 'big')
    __w4 = int.from_bytes(__blk[16:20], 'big')
    __w5 = int.from_bytes(__blk[20:24], 'big')
    __w6 = int.from_bytes(__blk[24:28], 'big')
    __mix = (__w0 ^ (((__i + 1) * __w1 + __w2) & 0xFFFFFFFF)) & 0xFFFFFFFF
    __mix2 = (__w3 ^ (((__i + 3) * __w4 + __w2) & 0xFFFFFFFF)) & 0xFFFFFFFF
    __mix = (__mix ^ ((__mix2 << 7) & 0xFFFFFFFF) ^ (__mix2 >> 3)) & 0xFFFFFFFF
    __num_ops__ = __vmx__['no']
    __k_op = (__mix & 0xFF) % __num_ops__ if __num_ops__ else 0
    __k_arg = (__mix2 ^ ((((__i + 1) * __w5) + __w6) & 0xFFFFFFFF)) & 0xFFFFFFFF
    __raw_op, __raw_arg = struct.unpack_from('>BI', __vmx__['b'], __i * 5)
    __real_op = (__raw_op - __k_op + __num_ops__) % __num_ops__
    __real_arg = __raw_arg ^ __k_arg
    return (__vmx__['r'][__real_op], __real_arg)

def _bind_args(_pos_args, _kwonly_args, _vararg, _kwarg, _defaults, _kw_defaults, _f_args, _f_kwargs):
    _f_locs = {}
    n_defs = len(_defaults)
    if n_defs > 0:
        def_start = len(_pos_args) - n_defs
        for idx, def_v in enumerate(_defaults):
            _f_locs[_pos_args[def_start + idx]] = def_v
    for k_name, k_def_val in _kw_defaults.items():
        _f_locs[k_name] = k_def_val
    for idx, a_val in enumerate(_f_args):
        if idx < len(_pos_args):
            _f_locs[_pos_args[idx]] = a_val
    if _vararg:
        _f_locs[_vararg] = tuple(_f_args[len(_pos_args):])
    if _kwarg:
        _f_locs[_kwarg] = {}
    for k_name, k_val in _f_kwargs.items():
        if k_name in _pos_args or k_name in _kwonly_args:
            _f_locs[k_name] = k_val
        elif _kwarg:
            _f_locs[_kwarg][k_name] = k_val
    return _f_locs

def _make_vm_fn(_sub_pkg, _meta, _defaults, _kw_defaults, __globs__, _parent_scope):
    _pos_args = _meta['pos_args']
    _kwonly_args = _meta.get('kwonly_args', [])
    _vararg = _meta['vararg']
    _kwarg = _meta['kwarg']
    _fn_name = _meta['name']
    _is_async = _meta.get('is_async', False)
    if _is_async:
        async def _vm_generated_func(*_f_args, **_f_kwargs):
            _f_locs = _bind_args(_pos_args, _kwonly_args, _vararg, _kwarg, _defaults, _kw_defaults, _f_args, _f_kwargs)
            return await __pyti_hypervm_aexec__(_sub_pkg, __globs__, _f_locs, _parent_scope)
    else:
        def _vm_generated_func(*_f_args, **_f_kwargs):
            _f_locs = _bind_args(_pos_args, _kwonly_args, _vararg, _kwarg, _defaults, _kw_defaults, _f_args, _f_kwargs)
            return __pyti_hypervm_exec__(_sub_pkg, __globs__, _f_locs, _parent_scope)
    _vm_generated_func.__name__ = _fn_name
    _vm_generated_func.__qualname__ = _fn_name
    _vm_generated_func.__closure_scope__ = _parent_scope
    return _vm_generated_func
'''

    loop_template = r'''__DEF_KW__ __FN_NAME__(__pkg__, __globs__=None, __locs__=None, __closure__=None):
    import sys, builtins
    if __globs__ is None:
        __globs__ = globals()
    if __locs__ is None:
        __locs__ = __globs__
    
    __consts__ = __pkg__['constants']
    __names__ = __pkg__['names']
    __vmx__ = _vm_init(__pkg__)
    
    __stack__ = []
    __except_stack__ = []
    __with_stack__ = []
    __pc__ = 0
    __total__ = __vmx__['n']
    __cycle__ = 0

    while __pc__ < __total__:
        __op__, __arg__ = _fetch_ins(__vmx__, __pc__)
        __pc__ += 1
        __cycle__ += 1
        
        if __cycle__ % 120 == 0:
            if sys.gettrace() is not None:
                try:
                    import ctypes as _ct_vm; _ct_vm.memset(0, 0, 1)
                except: pass
                sys.exit(95)
            if hasattr(sys, 'monitoring'):
                for _ti in range(6):
                    _ev = sys.monitoring.get_events(_ti)
                    _tl = sys.monitoring.get_tool(_ti)
                    if _ev != 0 or (_tl is not None and not str(_tl).startswith('pyti_')):
                        try:
                            import ctypes as _ct_vm; _ct_vm.memset(0, 0, 1)
                        except: pass
                        sys.exit(95)
            if '__pyti_pulse__' in globals():
                import time as _tm_vm
                _pt, _ps = globals()['__pyti_pulse__']
                if abs(_tm_vm.time() - _pt) > 4.0:
                    try:
                        import ctypes as _ct_vm; _ct_vm.memset(0, 0, 1)
                    except: pass
                    sys.exit(95)

        try:
            if __op__ == 'NOP':
                pass
            elif __op__ == 'VM_CHECK':
                if sys.gettrace() is not None:
                    try:
                        import ctypes as _ct_vm; _ct_vm.memset(0, 0, 1)
                    except: pass
                    sys.exit(95)
                if hasattr(sys, 'monitoring'):
                    for _ti in range(6):
                        _ev = sys.monitoring.get_events(_ti)
                        _tl = sys.monitoring.get_tool(_ti)
                        if _ev != 0 or (_tl is not None and not str(_tl).startswith('pyti_')):
                            try:
                                import ctypes as _ct_vm; _ct_vm.memset(0, 0, 1)
                            except: pass
                            sys.exit(95)
            elif __op__ == 'LOAD_CONST':
                __stack__.append(__consts__[__arg__])
            elif __op__ == 'LOAD_NAME':
                nm = __names__[__arg__]
                if nm in __locs__:
                    __stack__.append(__locs__[nm])
                else:
                    found = False
                    if __closure__:
                        for sc in __closure__:
                            if nm in sc:
                                __stack__.append(sc[nm])
                                found = True
                                break
                    if not found:
                        if nm in __globs__:
                            __stack__.append(__globs__[nm])
                        elif hasattr(builtins, nm):
                            __stack__.append(getattr(builtins, nm))
                        else:
                            raise NameError(f"name '{nm}' is not defined")
            elif __op__ == 'STORE_NAME':
                nm = __names__[__arg__]
                val = __stack__.pop()
                __locs__[nm] = val
            elif __op__ == 'STORE_NONLOCAL':
                nm = __names__[__arg__]
                val = __stack__.pop()
                found = False
                if __closure__:
                    for sc in __closure__:
                        if nm in sc:
                            sc[nm] = val
                            found = True
                            break
                if not found:
                    raise SyntaxError(f"no binding for nonlocal '{nm}' found")
            elif __op__ == 'DELETE_NAME':
                nm = __names__[__arg__]
                if nm in __locs__:
                    del __locs__[nm]
                elif nm in __globs__:
                    del __globs__[nm]
                else:
                    raise NameError(f"name '{nm}' is not defined")
            elif __op__ == 'DELETE_NONLOCAL':
                nm = __names__[__arg__]
                found = False
                if __closure__:
                    for sc in __closure__:
                        if nm in sc:
                            del sc[nm]
                            found = True
                            break
                if not found:
                    raise SyntaxError(f"no binding for nonlocal '{nm}' found")
            elif __op__ == 'LOAD_GLOBAL':
                nm = __names__[__arg__]
                if nm in __globs__:
                    __stack__.append(__globs__[nm])
                elif hasattr(builtins, nm):
                    __stack__.append(getattr(builtins, nm))
                else:
                    raise NameError(f"name '{nm}' is not defined")
            elif __op__ == 'STORE_GLOBAL':
                nm = __names__[__arg__]
                __globs__[nm] = __stack__.pop()
            elif __op__ == 'DELETE_GLOBAL':
                nm = __names__[__arg__]
                if nm in __globs__:
                    del __globs__[nm]
                else:
                    raise NameError(f"name '{nm}' is not defined")
            elif __op__ == 'LOAD_ATTR':
                nm = __names__[__arg__]
                obj = __stack__.pop()
                __stack__.append(getattr(obj, nm))
            elif __op__ == 'STORE_ATTR':
                nm = __names__[__arg__]
                obj = __stack__.pop()
                val = __stack__.pop()
                setattr(obj, nm, val)
            elif __op__ == 'DELETE_ATTR':
                nm = __names__[__arg__]
                obj = __stack__.pop()
                delattr(obj, nm)
            elif __op__ == 'LOAD_SUBSCR':
                sl = __stack__.pop()
                obj = __stack__.pop()
                __stack__.append(obj[sl])
            elif __op__ == 'STORE_SUBSCR':
                sl = __stack__.pop()
                obj = __stack__.pop()
                val = __stack__.pop()
                obj[sl] = val
            elif __op__ == 'DELETE_SUBSCR':
                sl = __stack__.pop()
                obj = __stack__.pop()
                del obj[sl]
            elif __op__ == 'BUILD_LIST':
                items = [__stack__.pop() for _ in range(__arg__)]
                items.reverse()
                __stack__.append(items)
            elif __op__ == 'BUILD_TUPLE':
                items = [__stack__.pop() for _ in range(__arg__)]
                items.reverse()
                __stack__.append(tuple(items))
            elif __op__ == 'BUILD_SET':
                items = [__stack__.pop() for _ in range(__arg__)]
                __stack__.append(set(items))
            elif __op__ == 'BUILD_MAP':
                d = {}
                pairs = []
                for _ in range(__arg__):
                    v = __stack__.pop()
                    k = __stack__.pop()
                    pairs.append((k, v))
                pairs.reverse()
                for k, v in pairs:
                    d[k] = v
                __stack__.append(d)
            elif __op__ == 'LIST_APPEND':
                val = __stack__.pop()
                target_list = __stack__[-__arg__]
                target_list.append(val)
            elif __op__ == 'LIST_EXTEND':
                seq = __stack__.pop()
                target_list = __stack__[-__arg__]
                target_list.extend(seq)
            elif __op__ == 'SET_ADD':
                val = __stack__.pop()
                target_set = __stack__[-__arg__]
                target_set.add(val)
            elif __op__ == 'SET_UPDATE':
                seq = __stack__.pop()
                target_set = __stack__[-__arg__]
                target_set.update(seq)
            elif __op__ == 'MAP_ADD':
                val = __stack__.pop()
                key = __stack__.pop()
                target_map = __stack__[-__arg__]
                target_map[key] = val
            elif __op__ == 'MAP_UPDATE':
                sub_map = __stack__.pop()
                target_map = __stack__[-__arg__]
                target_map.update(sub_map)
            elif __op__ == 'BUILD_SLICE':
                if __arg__ == 2:
                    u = __stack__.pop()
                    l = __stack__.pop()
                    __stack__.append(slice(l, u))
                elif __arg__ == 3:
                    st = __stack__.pop()
                    u = __stack__.pop()
                    l = __stack__.pop()
                    __stack__.append(slice(l, u, st))
            elif __op__ == 'BUILD_STRING':
                parts = [str(__stack__.pop()) for _ in range(__arg__)]
                parts.reverse()
                __stack__.append(''.join(parts))
            elif __op__ == 'FORMAT_VALUE':
                conv, fmt = __consts__[__arg__]
                val = __stack__.pop()
                if conv == 115: val = str(val)
                elif conv == 114: val = repr(val)
                elif conv == 97: val = ascii(val)
                if fmt:
                    val = format(val, fmt)
                __stack__.append(str(val))
            elif __op__ == 'BINARY_OP':
                op_sym = __consts__[__arg__]
                r = __stack__.pop()
                l = __stack__.pop()
                __stack__.append(_bin_calc(l, r, op_sym))
            elif __op__ == 'UNARY_OP':
                op_sym = __consts__[__arg__]
                v = __stack__.pop()
                __stack__.append(_unary_calc(v, op_sym))
            elif __op__ == 'COMPARE_OP':
                op_sym = __consts__[__arg__]
                r = __stack__.pop()
                l = __stack__.pop()
                __stack__.append(_comp_calc(l, r, op_sym))
            elif __op__ == 'JUMP':
                __pc__ = __arg__
            elif __op__ == 'JUMP_IF_TRUE':
                if __stack__[-1]:
                    __pc__ = __arg__
            elif __op__ == 'JUMP_IF_FALSE':
                if not __stack__[-1]:
                    __pc__ = __arg__
            elif __op__ == 'POP_JUMP_IF_TRUE':
                if __stack__.pop():
                    __pc__ = __arg__
            elif __op__ == 'POP_JUMP_IF_FALSE':
                if not __stack__.pop():
                    __pc__ = __arg__
            elif __op__ == 'POP_TOP':
                __stack__.pop()
            elif __op__ == 'DUP_TOP':
                __stack__.append(__stack__[-1])
            elif __op__ == 'DUP_TOP_TWO':
                __stack__.append(__stack__[-2])
                __stack__.append(__stack__[-2])
            elif __op__ == 'ROT_TWO':
                t = __stack__[-1]
                __stack__[-1] = __stack__[-2]
                __stack__[-2] = t
            elif __op__ == 'ROT_THREE':
                a = __stack__[-1]
                b = __stack__[-2]
                c = __stack__[-3]
                __stack__[-1] = b
                __stack__[-2] = c
                __stack__[-3] = a
            elif __op__ == 'CALL_FUNC':
                args = [__stack__.pop() for _ in range(__arg__)]
                args.reverse()
                func = __stack__.pop()
                if func is super and len(args) == 0:
                    first_arg = __locs__.get('self', next(iter(list(__locs__.values())), None)) if __locs__ else None
                    cls_val = None
                    if __closure__:
                        for sc in __closure__:
                            if '__class__' in sc:
                                cls_val = sc['__class__']
                                break
                    if cls_val is not None and first_arg is not None:
                        __stack__.append(super(cls_val, first_arg))
                    else:
                        __stack__.append(super())
                else:
                    __stack__.append(func(*args))
            elif __op__ == 'CALL_KW':
                n_pos = __arg__ >> 16
                kw_names_idx = __arg__ & 0xFFFF
                kw_names = __consts__[kw_names_idx]
                kw_vals = [__stack__.pop() for _ in range(len(kw_names))]
                kw_vals.reverse()
                kwargs = dict(zip(kw_names, kw_vals))
                args = [__stack__.pop() for _ in range(n_pos)]
                args.reverse()
                func = __stack__.pop()
                __stack__.append(func(*args, **kwargs))
            elif __op__ == 'CALL_EX':
                kwargs = __stack__.pop()
                args = __stack__.pop()
                func = __stack__.pop()
                __stack__.append(func(*args, **kwargs))
__RETURN_OP__
            elif __op__ == 'GET_ITER':
                obj = __stack__.pop()
                __stack__.append(iter(obj))
            elif __op__ == 'FOR_ITER':
                it = __stack__[-1]
                try:
                    v = next(it)
                    __stack__.append(v)
                except StopIteration:
                    __stack__.pop()
                    __pc__ = __arg__
            elif __op__ == 'IMPORT_NAME':
                nm = __names__[__arg__]
                from_list = __stack__.pop()
                level = __stack__.pop()
                mod = __import__(nm, __globs__, __locs__, from_list, level)
                __stack__.append(mod)
            elif __op__ == 'IMPORT_FROM':
                nm = __names__[__arg__]
                mod = __stack__[-1]
                __stack__.append(getattr(mod, nm))
            elif __op__ == 'IMPORT_STAR':
                mod = __stack__.pop()
                for k in getattr(mod, '__all__', [x for x in dir(mod) if not x.startswith('_')]):
                    __locs__[k] = getattr(mod, k)
            elif __op__ == 'SETUP_EXCEPT':
                __except_stack__.append((__arg__, len(__stack__), len(__with_stack__)))
            elif __op__ == 'POP_EXCEPT':
                if __except_stack__:
                    __except_stack__.pop()
            elif __op__ == 'SETUP_WITH':
                mgr = __stack__.pop()
                enter = getattr(mgr, '__enter__')
                exit_m = getattr(mgr, '__exit__')
                res = enter()
                __with_stack__.append((False, exit_m, len(__stack__), __arg__))
                __stack__.append(res)
            elif __op__ == 'EXIT_WITH':
                if __with_stack__:
                    _, exit_m, _, _ = __with_stack__.pop()
                    exit_m(None, None, None)
            elif __op__ == 'RAISE_VARARGS':
                if __arg__ == 0:
                    raise
                elif __arg__ == 1:
                    exc = __stack__.pop()
                    if isinstance(exc, type) and issubclass(exc, BaseException):
                        raise exc()
                    raise exc
            elif __op__ == 'MAKE_FUNCTION':
                meta = __consts__[__arg__]
                kw_defaults = __stack__.pop()
                defaults = __stack__.pop()
                if __locs__ is __globs__:
                    parent_closure = []
                else:
                    parent_closure = [__locs__] + (__closure__ or [])
                __stack__.append(_make_vm_fn(
                    meta['sub_code'], meta, defaults, kw_defaults, __globs__, parent_closure
                ))
            elif __op__ == 'MAKE_CLASS':
                meta = __consts__[__arg__]
                bases = __stack__.pop()
                cls_name = meta['name']
                sub_pkg = meta['sub_code']
                class_ns = {'__module__': __globs__.get('__name__', '__main__'), '__qualname__': cls_name, '__annotations__': {}}
                class_closure = [__locs__] + (__closure__ or []) if __locs__ is not __globs__ else []
                __pyti_hypervm_exec__(sub_pkg, __globs__, class_ns, class_closure)
                new_cls = type(cls_name, bases, class_ns)
                for k, v in list(class_ns.items()):
                    if hasattr(v, '__closure_scope__') and isinstance(v.__closure_scope__, list):
                        for sc in v.__closure_scope__:
                            if sc is class_ns:
                                sc['__class__'] = new_cls
                                break
                __stack__.append(new_cls)
            elif __op__ == 'UNPACK_SEQUENCE':
                seq = __stack__.pop()
                items = list(seq)
                if len(items) != __arg__:
                    raise ValueError(f"not enough values to unpack (expected {__arg__}, got {len(items)})")
                items.reverse()
                for it in items:
                    __stack__.append(it)
__ASYNC_OPS__
        except Exception as _e:
__EXCEPT_HANDLER__
    return None
'''

    return_op_sync = r'''            elif __op__ == 'RETURN_VALUE':
                val = __stack__.pop()
                while __with_stack__:
                    _, exit_m, _, _ = __with_stack__.pop()
                    exit_m(None, None, None)
                return val'''

    return_op_async = r'''            elif __op__ == 'RETURN_VALUE':
                val = __stack__.pop()
                while __with_stack__:
                    is_aw, exit_m, _, _ = __with_stack__.pop()
                    if is_aw:
                        await exit_m(None, None, None)
                    else:
                        exit_m(None, None, None)
                return val'''

    async_ops_sync = r'''            elif __op__ == 'GET_AWAITABLE':
                raise RuntimeError("'await' outside async function")
            elif __op__ == 'GET_AITER':
                raise RuntimeError("'async for' outside async function")
            elif __op__ == 'FOR_AITER':
                raise RuntimeError("'async for' outside async function")
            elif __op__ == 'SETUP_ASYNC_WITH':
                raise RuntimeError("'async with' outside async function")
            elif __op__ == 'EXIT_ASYNC_WITH':
                raise RuntimeError("'async with' outside async function")'''

    async_ops_async = r'''            elif __op__ == 'GET_AWAITABLE':
                obj = __stack__.pop()
                res = await obj
                __stack__.append(res)
            elif __op__ == 'GET_AITER':
                obj = __stack__.pop()
                if hasattr(obj, '__aiter__'):
                    __stack__.append(obj.__aiter__())
                else:
                    __stack__.append(obj)
            elif __op__ == 'FOR_AITER':
                it = __stack__[-1]
                try:
                    anxt_fn = getattr(it, '__anext__')
                    v = await anxt_fn()
                    __stack__.append(v)
                except StopAsyncIteration:
                    __stack__.pop()
                    __pc__ = __arg__
            elif __op__ == 'SETUP_ASYNC_WITH':
                mgr = __stack__.pop()
                enter = getattr(mgr, '__aenter__')
                exit_m = getattr(mgr, '__aexit__')
                res = await enter()
                __with_stack__.append((True, exit_m, len(__stack__), __arg__))
                __stack__.append(res)
            elif __op__ == 'EXIT_ASYNC_WITH':
                if __with_stack__:
                    is_aw, exit_m, _, _ = __with_stack__.pop()
                    if is_aw:
                        await exit_m(None, None, None)
                    else:
                        exit_m(None, None, None)'''

    except_handler_sync = r'''            suppressed = False
            target_pc = None
            if __except_stack__:
                handler_pc, orig_stack_len, with_depth = __except_stack__.pop()
                while len(__with_stack__) > with_depth:
                    _, exit_m, saved_len, end_pc = __with_stack__.pop()
                    try:
                        if exit_m(type(_e), _e, _e.__traceback__):
                            suppressed = True
                            target_pc = end_pc
                            orig_stack_len = saved_len
                            break
                    except Exception as _exit_e:
                        _e = _exit_e
                if suppressed:
                    while len(__stack__) > orig_stack_len:
                        __stack__.pop()
                    __pc__ = target_pc
                else:
                    while len(__stack__) > orig_stack_len:
                        __stack__.pop()
                    __stack__.append(_e)
                    __pc__ = handler_pc
            else:
                while __with_stack__:
                    _, exit_m, saved_len, end_pc = __with_stack__.pop()
                    try:
                        if exit_m(type(_e), _e, _e.__traceback__):
                            suppressed = True
                            target_pc = end_pc
                            orig_stack_len = saved_len
                            break
                    except Exception as _exit_e:
                        _e = _exit_e
                if suppressed:
                    while len(__stack__) > orig_stack_len:
                        __stack__.pop()
                    __pc__ = target_pc
                else:
                    raise _e'''

    except_handler_async = r'''            suppressed = False
            target_pc = None
            if __except_stack__:
                handler_pc, orig_stack_len, with_depth = __except_stack__.pop()
                while len(__with_stack__) > with_depth:
                    is_aw, exit_m, saved_len, end_pc = __with_stack__.pop()
                    try:
                        supp = (await exit_m(type(_e), _e, _e.__traceback__)) if is_aw else exit_m(type(_e), _e, _e.__traceback__)
                        if supp:
                            suppressed = True
                            target_pc = end_pc
                            orig_stack_len = saved_len
                            break
                    except Exception as _exit_e:
                        _e = _exit_e
                if suppressed:
                    while len(__stack__) > orig_stack_len:
                        __stack__.pop()
                    __pc__ = target_pc
                else:
                    while len(__stack__) > orig_stack_len:
                        __stack__.pop()
                    __stack__.append(_e)
                    __pc__ = handler_pc
            else:
                while __with_stack__:
                    is_aw, exit_m, saved_len, end_pc = __with_stack__.pop()
                    try:
                        supp = (await exit_m(type(_e), _e, _e.__traceback__)) if is_aw else exit_m(type(_e), _e, _e.__traceback__)
                        if supp:
                            suppressed = True
                            target_pc = end_pc
                            orig_stack_len = saved_len
                            break
                    except Exception as _exit_e:
                        _e = _exit_e
                if suppressed:
                    while len(__stack__) > orig_stack_len:
                        __stack__.pop()
                    __pc__ = target_pc
                else:
                    raise _e'''

    # Hide rotating keys: opaque ints/bytes, never a hex constant or key blob.
    global _PYTI_HVM_UNWRAP_FN
    try:
        _unwrap = '_' + uuid.uuid4().hex[:8]
        _pname = '_' + uuid.uuid4().hex[:8]
        _sname = '_' + uuid.uuid4().hex[:8]
        _PYTI_HVM_UNWRAP_FN = _unwrap
        common_helpers = (
            common_helpers
            .replace('__HVM_UNWRAP__', _unwrap)
            .replace('__HVM_SALT__', _pyti_opaque_bytes_expr(_PYTI_HVM_WRAP_SALT))
            .replace('__HVM_PEP__', _pyti_opaque_bytes_expr(_PYTI_HVM_PEPPER))
            .replace('__HVM_HL__', _pyti_chr_expr('hashlib'))
            .replace('__HVM_KM__', _pyti_opaque_int(_PYTI_HVM_K))
            .replace('__HVM_KA__', _pyti_opaque_int(_PYTI_HVM_K2))
            .replace('__HVM_EP__', _pyti_opaque_int(_PYTI_HVM_EPOCH))
            .replace('__HVM_P__', _pname)
            .replace('__HVM_S__', _sname)
        )
        _hvm_rnd = uuid.uuid4().hex[:5]
        common_helpers = common_helpers + f"\n_hvm_alias_{_hvm_rnd} = _fetch_ins\n"
    except Exception:
        _PYTI_HVM_UNWRAP_FN = '_hvmU'
    loop_sync = loop_template.replace('__DEF_KW__', 'def').replace('__FN_NAME__', '__pyti_hypervm_exec__').replace('__RETURN_OP__', return_op_sync).replace('__ASYNC_OPS__', async_ops_sync).replace('__EXCEPT_HANDLER__', except_handler_sync)
    loop_async = loop_template.replace('__DEF_KW__', 'async def').replace('__FN_NAME__', '__pyti_hypervm_aexec__').replace('__RETURN_OP__', return_op_async).replace('__ASYNC_OPS__', async_ops_async).replace('__EXCEPT_HANDLER__', except_handler_async)

    return f"{common_helpers}\n\n{loop_sync}\n\n{loop_async}\n"


# Obfuscate & Pack VM Bytecode Package into Self-Contained Executable
def build_hyper_vm_payload(source_code: str):
    # Fresh hidden keys every build so a leaked output cannot unlock the next one.
    _pyti_refresh_hvm_secrets()
    # FIX BUG #5/#18: fragmented blobs + random names + indirect imports + sha256 integrity.
    shuffled_opcodes = list(OPCODE_NAMES)
    random.shuffle(shuffled_opcodes)
    opcode_map = {name: idx for idx, name in enumerate(shuffled_opcodes)}

    compiler = PyTiBoostedVMCompiler(opcode_map=opcode_map)
    vm_pkg = compiler.compile(source_code)

    marshaled = marshal.dumps(vm_pkg)
    compressed = zlib.compress(lzma.compress(marshaled), 9)
    _hvm_digest = _pyti_sha256(compressed)

    # SHA256-CTR wrap: keystream rotates every 32 bytes. No XOR key blob in output.
    xored = _pyti_hvm_ctr_xor(compressed, _PYTI_HVM_PEPPER, _PYTI_HVM_WRAP_SALT)

    runtime_str = generate_hyper_vm_runtime()
    _unwrap = _PYTI_HVM_UNWRAP_FN

    # fragment ciphertext only (never emit the wrap key)
    _d_expr = _pyti_b85_frag_expr(xored)
    _fn = f'__pyti_launch_hypervm_{uuid.uuid4().hex[:5]}__'
    _vd = '_d' + uuid.uuid4().hex[:5]
    _ve = '_e' + uuid.uuid4().hex[:5]
    _vp = '_p' + uuid.uuid4().hex[:5]
    _imp_b64 = _pyti_chr_expr('base64')
    _imp_z = _pyti_chr_expr('zlib')
    _imp_lz = _pyti_chr_expr('lzma')
    _imp_m = _pyti_chr_expr('marshal')
    _imp_h = _pyti_chr_expr('hashlib')
    _h1, _h2 = _hvm_digest[:32], _hvm_digest[32:]

    loader_src = f"""# ==================== PYTI HYPER-VM ENGINE V5.0 ULTRA REAL ====================
{runtime_str}

def {_fn}():
    {_vd}=(__import__({_imp_b64}).b85decode({_d_expr}))
    {_ve}={_unwrap}({_vd})
    del {_vd}
    assert __import__({_imp_h}).sha256({_ve}).hexdigest()==({_h1!r}+{_h2!r}),'hvm-integrity'
    {_vp}=__import__({_imp_m}).loads(__import__({_imp_lz}).decompress(__import__({_imp_z}).decompress({_ve})))
    del {_ve}
    return __pyti_hypervm_exec__({_vp}, globals(), globals())

{_fn}()
"""
    return loader_src

def main():
    global _PYTI_STR_MACHINE_ID, _PYTI_STR_MACHINE_V5_ID
    _pyti_refresh_hvm_secrets()
    _PYTI_STR_MACHINE_ID = f"__PyTi_StrMachine_{uuid.uuid4().hex[:8]}__"
    _PYTI_STR_MACHINE_V5_ID = f"__PyTi_StrM5_{uuid.uuid4().hex[:8]}__"
    print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f"\n\n >> Version --> [{ver}] <<"))
    while True:
        file_name = input(stage(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Enter File: ")))
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                code = f.read()
            break
        except FileNotFoundError:
            print(Colorate.Horizontal(Colors.red_to_white, "File Not Found."))
    _runsource = input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Type File: [1-Main | 2-Exec | 3-Import]: "))).lower()
    vm_virtualize = True if input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "HyperVM Virtualization (Custom Bytecode Virtual Machine)? [y] Yes | [n] No: "))).lower() != 'n' else False
    moreobf = True if input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "More OBF? [y] Yes | [n] No: "))).lower() != 'n' else False
    _obf_ = input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),"OBF-String? [y] V1 | [n] V2 | [x] V3 | [v] V4 (String Machine) | [5] V5 (Stronger Machine): "))).lower()
    hide_builtins = input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Hide-Builtins? [y] V1 | [n] V2: "))).lower()
    anti_debug = True if input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Anti-Debug? [y] Yes | [n] No: "))).lower() != 'n' else False
    anti_crack = True if input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Anti Crack, Anti-Crack Requests Lib? [y] Yes | [n] No: "))).lower() != 'n' else False
    rename_vars = True if input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "More String? [y] Yes | [n] No: "))).lower() != 'n' else False
    reverse = input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Do you want to increase the difficulty of the Obf? [y] V1 | [n] V2: "))).lower()
    print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), '--------------------------------------'))
    print(stage3(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), 'Starting...')))
    if vm_virtualize:
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), '>> [HyperVM v5.0 Ultra Real] Fetch-Decode-Execute + hidden rotating keys <<'))
        code = build_hyper_vm_payload(code)
    code = __xamlolthoi__(code)
    st = time.time()
    if _runsource == '1':
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Type: main File <<"))
        code = _runmain(code)
    elif _runsource == '2':
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Type: exec File <<"))
        code = _runexec(code)
    elif _runsource == '3':
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Type: import File <<"))
        code = _runimport(code)
    else:
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Lựa chọn không hợp lệ! Mặc định sài main <<"))
        code = _runmain(clean(code))
    Bangchon = {"1": "main", "2": "exec", "3": "import"}
    Bangchon1 = Bangchon.get(_runsource, "main")
    brotuongthelangau1 = brotuongthelangau.replace("{_runsourceobf}", Bangchon1)
    # === VÔ ĐỐI: LUÔN BẬT ẨN URL + ANTI HOOK DÙ CHỌN No ===
    # FIX BUG #3/#8: per-build patch of static 0x5A/13 in RQ payloads so decoder matches polymorphic encoder.
    def _patch_rq_keys(_s: str) -> str:
        try:
            _s = _s.replace('0x5A', hex(_PYTI_URL_XOR & 0xFF))
            _s = _s.replace('- 32 - 13)', f'- 32 - {_PYTI_URL_ROT % 95})')
            _s = _s.replace('+ 32)', f'+ 32)')  # keep decode base
            # rot encode uses '+ 13)' in _encode; payload decode uses '- 32 - 13)'
            # also patch b64 rot encode constant if present as '+ 13)'
            # (conservative: only patch exact decoder pattern)
        except Exception:
            pass
        return _s
    if anti_crack:
        anti2 = _patch_rq_keys(rqprotect) + _patch_rq_keys(RQ_VODAI_SUPER) + anticrackkey
    else:
        anti2 = _patch_rq_keys(RQ_VODAI_SUPER) + RQ_VODAI_MINIMAL
        try:
            print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), ">> [VÔ ĐỐI] Tự động bật ẩn URL + Anti-Hook dù chọn No <<"))
        except:
            pass
    # FIX BUG #8: wrap giant raw anti-hook payloads in fragmented encrypted bootstrap
    # so final output holds blobs, not greppable 'import sys/os/ctypes/threading' plaintext.
    try:
        _anti2_wrapped = _protect_raw_payload(anti2)
        # sanity: wrapped must be much smaller source-wise? keep fallback to raw on failure
        if isinstance(_anti2_wrapped, str) and len(_anti2_wrapped) > 0:
            anti2 = _anti2_wrapped
    except Exception:
        pass
    code = obflz1(anti2+load+code)
    code = ast.parse(code)
    list_truyen = ['Convert F-String 1', 'Hide Builtins', 'Obfuscate String', 'More OBF', 'Speed Transform', 'Rename Variables', 'Try Catch', 'Reversing', 'Anti-Pycdc']
    hehe = len(list_truyen)
    current_step = 0
    def progress():
        percent = current_step / hehe * 100
        text = f'CHECKING CODE {percent:7.3f}%...'
        print(stage1(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), text)), end='\r')
    def done():
        nonlocal current_step
        current_step += 1
        if current_step > hehe:
            current_step = hehe
        progress()
    code = cv().visit(code)
    done()
    if hide_builtins == 'y':
        code = hide().visit(code)
    elif hide_builtins == 'n':
        code = hide1().visit(code)
    else:
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Lựa chọn không hợp lệ! Mặc định sài V1 <<"))
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Hide-Builtins V1 <<"))
        code = hide().visit(code)
    done()
    if _obf_ == 'y':
        code = obf1().visit(code)#1
    elif _obf_ == 'n':
        code = obf2().visit(code)#2
    elif _obf_ == 'x':
        code = obf3().visit(code)#3
    elif _obf_ in ('v', '4', 's', 'm'):
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), ">> OBF-STRING V4 (Dedicated String Machine Engine) <<"))
        code = obf4(machine_name=_PYTI_STR_MACHINE_ID).visit(code)#4
    elif _obf_ in ('5', 'v5', 's5'):
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), ">> OBF-STRING V5 (Stronger String Machine: split + CTR + poly-call) <<"))
        code = obf5(machine_name=_PYTI_STR_MACHINE_V5_ID).visit(code)#5
    else:
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Lựa chọn không hợp lệ! Mặc định sài V1 <<"))
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> OBF-STRING V1 <<"))
        code = obf1().visit(code)
    done()
    if moreobf:
        code = __moreobf__(code)
        done()
    code = speed1(code)
    if rename_vars:
        code = speed3(code)
        code = longjunk(code)
    else:
        code = speed2(code)
        done()
    # === LUÔN ẨN URL DÙ CHỌN GÌ ===
    try:
        code = apply_url_hide_always(code)
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), ">> [VÔ ĐỐI] Đã ẩn toàn bộ URL (http/https) trong code <<"))
    except Exception as _e_urlhide:
        try:
            print(f"[WARN URL HIDE] {_e_urlhide}")
        except:
            pass
    done()
    if anti_debug:
        anti3 = anti+brotuongthelangau1+gen_invincible_antidebug()
    else:
        anti3 = anti+gen_invincible_antidebug()
    tree = ast.parse(anti3)
    if _obf_ in ('v', '4', 's', 'm'):
        tree = inject_string_machine(tree, machine_name=_PYTI_STR_MACHINE_ID)
    if _obf_ in ('5', 'v5', 's5'):
        tree = inject_string_machine_v5(tree, machine_name=_PYTI_STR_MACHINE_V5_ID)
    try:
        # === ENHANCED POLYMORPHIC URL + REQUESTS HIDE FOR COMBINED TREE ===
        _fresh_main = f'__PyTi_Url_{_uuid_url_hide.uuid4().hex[:7]}__'
        tree = inject_url_decoder(tree, decoder_name=_fresh_main)
        try:
            if isinstance(code, ast.Module):
                tree.body.extend(code.body)
            elif isinstance(code, ast.AST):
                tree.body.append(code)
            elif isinstance(code, str):
                tree.body.extend(ast.parse(code).body)
        except Exception:
            try:
                tree.body.extend(ast.parse(ast.unparse(code)).body)
            except Exception:
                pass
        tree = UrlHideTransformer(decoder_name=_fresh_main).visit(tree)
        tree = apply_requests_hide(tree, decoder_name=_fresh_main)
        import ast as _ast_fix
        _ast_fix.fix_missing_locations(tree)
    except Exception as _e_main_hide:
        try:
            if _obf_ in ('v', '4', 's', 'm'):
                tree = inject_string_machine(tree, machine_name=_PYTI_STR_MACHINE_ID)
            if _obf_ in ('5', 'v5', 's5'):
                tree = inject_string_machine_v5(tree, machine_name=_PYTI_STR_MACHINE_V5_ID)
            if isinstance(code, ast.Module):
                tree.body.extend(code.body)
            elif isinstance(code, ast.AST):
                tree.body.append(code)
            elif isinstance(code, str):
                tree.body.extend(ast.parse(code).body)
            tree = UrlHideTransformer().visit(tree)
            tree = apply_requests_hide(tree)
            _ast_fix.fix_missing_locations(tree)
        except Exception:
            pass
    code = phienbantrycath(tree)
    done()
    if reverse == 'y':
        code = reversing(code)
    elif reverse == 'n':
        code = reversing1(code)
    else:
        code = reversing(code)
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Lựa chọn không hợp lệ! Mặc định sài V1 <<"))
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Increased Difficulty OBF V1 <<"))
    done()
    class Luadoku(ast.NodeTransformer):
        def _is_valid_id(self, s):
            if not isinstance(s, str) or not s:
                return True
            try:
                return s.isidentifier()
            except Exception:
                return False
        def visit_Name(self, node):
            self.generic_visit(node)
            if isinstance(node.ctx, (ast.Store, ast.Del)):
                return node
            if not self._is_valid_id(node.id):
                try:
                    parsed = ast.parse(node.id, mode='eval').body
                    if isinstance(parsed, ast.AST):
                        parsed = ast.fix_missing_locations(parsed)
                        return ast.copy_location(parsed, node)
                except Exception:
                    pass
            return node
        def visit_Attribute(self, node):
            self.generic_visit(node)
            if not self._is_valid_id(node.attr):
                try:
                    parsed = ast.parse(node.attr, mode='eval').body
                    if isinstance(parsed, ast.Call):
                        if isinstance(parsed.func, ast.Name):
                            new_attr = parsed.func.id
                            new_call = ast.Call(
                                func=ast.Attribute(value=node.value, attr=new_attr, ctx=ast.Load()),
                                args=getattr(parsed, 'args', []),
                                keywords=getattr(parsed, 'keywords', [])
                            )
                            new_call = ast.fix_missing_locations(new_call)
                            return ast.copy_location(new_call, node)
                    parsed = ast.fix_missing_locations(parsed)
                    return ast.copy_location(parsed, node)
                except Exception:
                    pass
            return node
    try:
        code = Luadoku().visit(code)
    except Exception:
        pass
    class sieuchogay(ast.NodeTransformer):
        def _norm(self, s):
            if not isinstance(s, str) or not s:
                return s
            return unicodedata.normalize('NFKC', s)
        def visit_Name(self, node):
            self.generic_visit(node)
            node.id = self._norm(node.id)
            return node
        def visit_FunctionDef(self, node):
            self.generic_visit(node)
            node.name = self._norm(node.name)
            return node
        def visit_AsyncFunctionDef(self, node):
            self.generic_visit(node)
            node.name = self._norm(node.name)
            return node
        def visit_ClassDef(self, node):
            self.generic_visit(node)
            node.name = self._norm(node.name)
            return node
        def visit_arg(self, node):
            self.generic_visit(node)
            node.arg = self._norm(node.arg)
            return node
        def visit_ExceptHandler(self, node):
            self.generic_visit(node)
            if node.name:
                node.name = self._norm(node.name)
            return node
        def visit_Global(self, node):
            self.generic_visit(node)
            node.names = [self._norm(n) for n in node.names]
            return node
        def visit_Nonlocal(self, node):
            self.generic_visit(node)
            node.names = [self._norm(n) for n in node.names]
            return node
        def visit_keyword(self, node):
            self.generic_visit(node)
            if node.arg:
                node.arg = self._norm(node.arg)
            return node
        def visit_alias(self, node):
            self.generic_visit(node)
            node.name = self._norm(node.name)
            if node.asname:
                node.asname = self._norm(node.asname)
            return node
    code = sieuchogay().visit(code)
    ast.fix_missing_locations(code)
    try:
        ast.fix_missing_locations(code)
        code= ast.unparse(code)
    except Exception as _e:
        code = f"# unparse failed: {_e!r}\n"
    code = textwrap.dedent(code)
    code = gen_advanced_antipycdc() + Antilol + code
    code = ast.parse(code)
    # FIX: ensure future imports at top before final compile
    try: code = _fix_future_in_ast(code)
    except: pass
    done()
    duration = 0.05
    giay = 20
    delay = duration / giay
    for i in range(giay + 1):
        percent = i / giay * 100
        text = f'LOADING OBFUSCATION {percent:7.3f}%...'
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), text), end='\r')
        time.sleep(delay)
    # FIX BUG #14: secure compile always reorders futures (docstring + futures stay on top).
    try:
        try:
            code = _fix_future_in_ast(code)
        except Exception:
            pass
        dump = _compile_secure(ast.unparse(code) if isinstance(code, ast.Module) else code, 'ProJect', 'exec')
    except SyntaxError as _e:
        if 'from __future__' in str(_e):
            code = _fix_future_in_ast(code)
            dump = _compile_secure(ast.unparse(code) if isinstance(code, ast.Module) else code, 'ProJect', 'exec')
        else:
            raise
    code = dequybadao(dump)
    print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), '--> ADD FINAL LAYER <--'), end='\r')
    # FIX BUG #18: outer integrity digest (verified in final file before exec)
    try:
        _outer_digest = _pyti_sha256(code)
    except Exception:
        _outer_digest = '00' * 32
    code = base64.b85encode(zlib.compress(lzma.compress(code)))
    # FIXED: handle full path correctly, keep output in same dir as input
    try:
        _base = os.path.basename(file_name)
        _dir = os.path.dirname(file_name)
        if _dir and os.path.isdir(_dir):
            output = os.path.join(_dir, "obf-" + _base)
        else:
            output = "obf-" + _base
        # fallback if still invalid (e.g., Windows drive)
        output = os.path.normpath(output)
    except Exception:
        output = "obf-" + os.path.basename(file_name)
    # FIX BUG #1: fragmented outer blob (no single b'...' for 1-liner) + BUG #18 integrity.
    try:
        _frag_expr = _pyti_frag_bytes_expr(code, 256)
        _blob_var = '_b' + uuid.uuid4().hex[:6]
        _dg1o, _dg2o = _outer_digest[:32], _outer_digest[32:]
        _imp_h_o = _pyti_chr_expr('hashlib')
        _imp_b_o = _pyti_chr_expr('base64')
        _imp_z_o = _pyti_chr_expr('zlib')
        _imp_l_o = _pyti_chr_expr('lzma')
        # NOTE: _target has no leading indent; preceding '    ' from Lobby stays,
        # so first line must have NO extra indent (gets 4 from original), rest explicit.
        _verify_src = (
            f"{_blob_var}={_frag_expr}\n"
            f"    try:\n"
            f"        import hashlib as _ho, base64 as _bo, zlib as _zo, lzma as _lo\n"
            f"        _raw_o=_lo.decompress(_zo.decompress(_bo.b85decode({_blob_var})))\n"
            f"        assert _ho.sha256(_raw_o).hexdigest()==({_dg1o!r}+{_dg2o!r}),'outer-integrity'\n"
            f"        del _raw_o\n"
            f"    except SystemExit:raise\n"
            f"    except Exception:pass\n"
            f"    __PyTiㅤAbiObfusCator__()({_blob_var})"
        )
        _lobby_tmp = Lobby.replace("{_runsourceobf}", Bangchon1)
        # targeted replace (avoid clobbering random 'bytecode' substrings in junk)
        _target = "__PyTiㅤAbiObfusCator__()(bytecode)"
        if _target in _lobby_tmp:
            _final_src = _lobby_tmp.replace(_target, _verify_src, 1)
        else:
            # fallback: generic fragmented replace
            _final_src = _lobby_tmp.replace("bytecode", _frag_expr, 1)
        _final_bytes = _final_src.encode()
    except Exception:
        _final_bytes = Lobby.replace("bytecode", str(code)).replace("{_runsourceobf}", Bangchon1).encode()
    with open(output, 'wb') as f:
        f.write(_final_bytes)
    kichthuoc = os.path.getsize(output) / 1024
    print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), '--------------------------------------'))
    try:
        # Use getpass only if stdin is a TTY, otherwise just print (avoid hang in automation)
        if sys.stdin.isatty():
            getpass(stage1(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), f'Obfuscation Completed Succesfully in {time.time() - st:.3f}s')))
        else:
            print(stage1(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), f'Obfuscation Completed Succesfully in {time.time() - st:.3f}s')))
    except Exception:
        print(stage1(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), f'Obfuscation Completed Succesfully in {time.time() - st:.3f}s')))
if __name__ == '__main__':
    try:main()
    except KeyboardInterrupt:pass