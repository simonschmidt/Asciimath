#!/usr/bin/python
# coding: utf-8
import re
import sys

alnum=u'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

# Sub and supscripts
sup=u"ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴿᵀᵁⱽᵂ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᵅᵝᵞᵟᵋᶿᶥᶲᵠᵡ"
supn=u"abcdefghijklmnoprstuvwxyzABDEGHIJKLMNOPRTUVW0123456789+-=()αβγδεθιΦφχ"
supd={u'^%s'%k: v for k,v in zip(supn,sup)}

sub=u"ₐₑₕᵢₖₗₘₙₒₚᵣₛₜᵤᵥₓ₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ᵦᵧᵨᵩᵪ"
subn=u"aehiklmnoprstuvx0123456789+-=()βιρφχ"
subd={u'_%s'%k: v for k,v in zip(subn,sub)}


# Mathematical symbols
mathd = {'\\infty': u'∞', '\\pd':      u'∂', '\\iint':     u'∬',
         '\\iiint': u'∭', '\\oiint':   u'∯', '\\oiiint':   u'∰',
         '\\int':   u'∫', '\\sum':     u'∑', '\\prod':     u'∏',
         '\\oint':  u'∮', '\\oo':      u'∞', '\\cap':      u'∩',
         '\\in':    u'∈', '\\exists':  u'∃', '\\nexists':  u'∄',
         '\\forall':u'∀', '\\empty':   u'∅', '\\laplace':  u'Δ',
         '\\nabla': u'∇', '\\ni':      u'∋', '\\!=':       u'≠',
         '\\<=':    u'≤', '\\>=':      u'≥', '\\+-':       u'±',
         '\\-+':    u'∓', '\\so':      u'∴', '\\since':    u'∵',
         '\\nni':   u'∌', '\\(+)':     u'⊕', '\\(-)':      u'⊖',
         '\\(*)':   u'⊗', '\\(/)':     u'⊘', '\\(.)':      u'⊙',
         '\\nin':   u'∉', '\\perp':    u'⊥', '\\prop':     u'∝',
         '\\left':  u'⇐', '\\iff':     u'⇔', '\\right':    u'⇒',
         '\\equiv': u'⇔', '\\implies': u'⇒', '\\limplies': u'⇐',
         '\\sqrt':  u'√', '\\wave':    u'∿', '\\div':      u'∣',
         '\\ndiv':  u'∤', '\\and':     u'∧', '\\or':       u'∨',
         '\\aleph': u'ℵ', '\\beth':    u'ℶ', '\\approx':   u'≈',
         '\\sim':   u'≈', '\\not':     u'¬', '\\subset':   u'⊂',
         '\\supset':u'⊃', '\\union':   u'∪', '\\cup':      u'∪',
         '\\cap':   u'∩', '\\mapsto':  u'↦', 
    }

escaped = {'\\_':   u'_', '\\^':       u'^', '\\\\':       u'\\'}

# Greek symbols
greekd ={'\\alpha': u'α', '\\beta':    u'β', '\\gamma':    u'γ',
         '\\delta': u'δ', '\\epsilon': u'ε', '\\zeta':     u'ζ',
         '\\eta':   u'η', '\\theta':   u'θ', '\\iota':     u'ι',
         '\\kappa': u'κ', '\\lambda':  u'λ', '\\mu':       u'μ',
         '\\nu':    u'ν', '\\xi':      u'ξ', '\\omicron':  u'ο',
         '\\pi':    u'π', '\\rho':     u'ρ', '\\sigma':    u'σ',
         '\\tau':   u'τ', '\\upsilon': u'υ', '\\phi':      u'φ',
         '\\chi':   u'χ', '\\psi':     u'ψ', '\\omega':    u'ω',
         '\\Alpha': u'Α', '\\Beta':    u'Β', '\\Gamma':    u'Γ',
         '\\Delta': u'Δ', '\\Epsilon': u'Ε', '\\Zeta':     u'Ζ',
         '\\Eta':   u'Η', '\\Theta':   u'Η', '\\Iota':     u'Ι',
         '\\Kappa': u'Κ', '\\Lambda':  u'Λ', '\\Mu':       u'Μ',
         '\\Nu':    u'Ν', '\\Xi':      u'Ξ', '\\Omicron':  u'Ο',
         '\\Pi':    u'Π', '\\Rho':     u'Ρ', '\\Sigma':    u'Σ',
         '\\Tau':   u'Τ', '\\Upsilon': u'Υ', '\\Phi':      u'Φ',
         '\\Chi':   u'Χ', '\\Psi':     u'Ψ', '\\Omega':    u'Ω',
        }



letters= u'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

types={
'bb': u'𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚ⅉ𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡'
,
'bo': u'𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗'
,
'it': u'𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧'
,
'boit': u'𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛'
,
'sc': u'𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏'
,
'bosc': u'𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃'
,
'fr': u'𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷'
,
'dost': u'𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫'
,
'bofr': u'𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟'
,
'ss': u'𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫'
,
'ssbo': u'𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵'
,
'ssit': u'𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻'
,
'ssboit': u'𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯'
,
'ms': u'𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿'
,
}

symbd = {}

symbd.update(greekd)
symbd.update(mathd)
symbd.update(supd)
symbd.update(subd)
for k,v in types.items():
    symbd.update({ (u'\\%s%s' % (k,n), s) for n,s in zip(alnum,v)})

testdict = symbd.copy()
testdict.update(escaped)
symbd = dict((re.escape(k),v) for k,v in symbd.iteritems())
escaped = dict((re.escape(k), v) for k,v in escaped.iteritems())
# To avoid \int getting parsed as (\in)t the regex will be 
# created from the revere alphanumeric sorting of the keys
symkey = sorted(symbd.keys(), reverse=True)
symkey = escaped.keys() + symkey
symbd.update(escaped)

pattern = re.compile(ur"(%s)" % "|".join(symkey),re.UNICODE)


def available():
    items=greekd.items()
    items=sorted(items,key=lambda x: x[0])

    print "Greek letters\n"
    for k,v in items:
        print u'%-10s | %s'%(k,v)

    items=mathd.items()
    items=sorted(items,key=lambda x: x[1])
    print '\nMathematical symbols\n'
    for k,v in items:
        print u'%-10s | %s'%(k,v)

    print u"\nSubscriptable _?: %s" % sub
    print u'Supscriptable ^?: %s' % sup
    print u"\nAlphanumerical symbols\n bo: bold, it: italic, sc: script, fr: fraktur, dost: double-struck, ss: sans-serif, ms: mono-space"

    items=types.items()
    items=sorted(items,key=lambda x: x[0])
    for k,v in items:
        print u'\\%-10s: %s'%(k,v)

def test():
    for k,v in testdict.items():
        if utf8ify(k) != v:
            print u"failed %s -> %s != %s"%(k,utf8ify(esc),v)

desc=u"""
Convert plain-text math to unicode

examples:
    $ asciimath '\\intf_1(x)f_2(x)d\\mu'
    ∫f₁(x)f₂(x)dμ

    $ asciimath 'cos(\\pi) = -1'
    cos(π) = -1

    $ asciimath 'q\\in\\bbB \\right q\\in\\bbR'
    q∈ℚ ⇒ q∈ℝ

    $ asciimath 'a^\\alpha = \\tau'
    aᵅ = τ

    $ asciimath 'x^a \\^a'
    xᵃ ^a

unicode-limitations:
    very few greek symbols are possible to sup and subscript
           supscriptable:  α β γ δ ε θ ι Φ φ χ
           subscriptable:  β ι ρ φ χ

    Capital letters are not possible to subscript at all
    Supscriptable capitals: A B D E G H I J K L M N O P R T U V W

    """
def utf8ify(text):
    return pattern.sub(lambda m: symbd[re.escape(m.group(0))], text)



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=desc,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-a','--all', help='Print all available symbols',action='store_true')
    parser.add_argument('-d','--debug',action='store_true')
    parser.add_argument('text', help='Text to convert',nargs='*')

    args = parser.parse_args()

    if args.all:
        available()
    elif args.debug:
        test()
    elif not args.text:
        parser.print_help()
    else:
        print utf8ify(u'\n'.join(args.text ))
    sys.exit()

