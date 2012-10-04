#!/usr/bin/python
# coding: utf-8
import re
import sys
import getopt

sup= u"ᵃ ᵇ ᶜ ᵈ ᵉ ᶠ ᵍ ʰ ⁱ ʲ ᵏ ˡ ᵐ ⁿ ᵒ ᵖ ʳ ˢ ᵗ ᵘ ᵛ ʷ ˣ ʸ ᶻ ᴬ ᴮ ᴰ ᴱ ᴳ ᴴ ᴵ ᴶ ᴷ ᴸ ᴹ ᴺ ᴼ ᴾ ᴿ ᵀ ᵁ ⱽ ᵂ ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁼ ⁽ ⁾ ᵅ ᵝ ᵞ ᵟ ᵋ ᶿ ᶥ ᶲ ᵠ ᵡ".split(' ')
supd=u"a b c d e f g h i j k l m n o p r s t u v w x y z A B D E G H I J K L M N O P R T U V W 0 1 2 3 4 5 6 7 8 9 + - = ( ) α β γ δ ε θ ι Φ φ χ".split(' ')

tosup = dict(zip(supd,sup))

sub = u"ₐ ₑ ₕ ᵢ ₖ ₗ ₘ ₙ ₒ ₚ ᵣ ₛ ₜ ᵤ ᵥ ₓ ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₊ ₋ ₌ ₍ ₎ ᵦ ᵧ ᵨ ᵩ ᵪ".split(' ')
subd= u"a e h i k l m n o p r s t u v x 0 1 2 3 4 5 6 7 8 9 + - = ( ) β ι ρ φ χ".split(' ')

tosub = dict(zip(subd,sub))

symbd = {   '\\infty': u'∞', '\\part':    u'∂',
            '\\int':   u'∫', '\\sum':     u'∑', '\\prod':     u'∏',
            '\\oint':  u'∮', '\\oo':      u'∞', '\\cap':      u'∩',
            '\\in':    u'∈', '\\exist':   u'∃', '\\forall':   u'∀',
            '\\nin':   u'∉', '\\perp':    u'⊥', '\\prop':     u'∝',
            '\\alpha': u'α', '\\beta':    u'β', '\\gamma':    u'γ',
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

symbd = dict((re.escape(k),v) for k,v in symbd.iteritems())
pattern = re.compile("(%s)" % "|".join(symbd.keys()))


def utf8ify(text):
    u"""
        Examples:
            utf8ify('\\int f_1(x)f_2(x)d\\mu') ->  '∫ f₁(x)f₂(x)dμ'
            utf8ify('cos(\\pi) = -1')          ->  'cos(π) = -1'
            utf8ify(u'a^\\alpha = \\tau')      ->  'aᵅ = τ'

        UTF8-limitations:
            very few greek symbols are possible to sup and subscript
                   supscriptable:  α β γ δ ε θ ι Φ φ χ
                   subscriptable:  β ι ρ φ χ

            Capital letters are not possible to subscript at all
            Supscriptable capitals: A B D E G H I J K L M N O P R T U V W


        Symbols:
            greek letters:       \\alpha  etc
            superscript letter:  ^
            subscript letter:    _
            math symbols:        \\int \\sum \\prod \\in \\exist \\forall
                                 \\nin \\perp \\prop

    """
    text = pattern.sub(lambda m: symbd[re.escape(m.group(0))], text)
    i = text.find('_')
    while not (i == -1 or i == len(text)-1) :
        if tosub.has_key(text[i+1]):
            text = text[:i] + tosub[text[i+1]] + text[i+2:]
            i = text.find('_',i)
        else:
            i = text.find('_',i+1)

    i = text.find('^')
    while not (i == -1 or i == len(text)-1 ):
        if tosup.has_key(text[i+1]):
            text = text[:i] + tosup[text[i+1]] + text[i+2:]
            i = text.find('^',i)
        else:
            i = text.find('_',i+1)

    return text


if __name__ == '__main__':
   print utf8ify(u' '.join(sys.argv[1:] ))
   sys.exit()
