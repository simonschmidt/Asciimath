Asciimath
=========

Converts ascii math to utf8
##Examples
        $ asciimath '\int f_1(x)f_2(x)d\mu'
        ∫ f₁(x)f₂(x)dμ
        $ asciimath 'cos(\pi) = -1'
        'cos(π) = -1'
        $ asciimath 'a^\\alpha = \\tau'
        'aᵅ = τ'

##UTF8-limitations
        very few greek symbols are possible to sup and subscript
            supscriptable:  α β γ δ ε θ ι Φ φ χ
            subscriptable:  β ι ρ φ χ

        Capital letters are not possible to subscript at all
        Supscriptable capitals: A B D E G H I J K L M N O P R T U V W

        All subscriptable:
        ₐ ₑ ₕ ᵢ ₖ ₗ ₘ ₙ ₒ ₚ ᵣ ₛ ₜ ᵤ ᵥ ₓ ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₊ ₋ ₌ ₍ ₎ ᵦ ᵧ ᵨ ᵩ ᵪ
        All supscriptable:
        ᵃ ᵇ ᶜ ᵈ ᵉ ᶠ ᵍ ʰ ⁱ ʲ ᵏ ˡ ᵐ ⁿ ᵒ ᵖ ʳ ˢ ᵗ ᵘ ᵛ ʷ ˣ ʸ ᶻ ᴬ ᴮ ᴰ ᴱ ᴳ ᴴ ᴵ ᴶ ᴷ ᴸ ᴹ ᴺ ᴼ ᴾ ᴿ ᵀ ᵁ ⱽ ᵂ ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁼ ⁽ ⁾ ᵅ ᵝ ᵞ ᵟ ᵋ ᶿ ᶥ ᶲ ᵠ ᵡ

##Symbols
        greek letters:       \\alpha  etc
        superscript letter:  ^
        subscript letter:    _
        math symbols:        \\int \\sum \\prod \\in \\exist \\forall
                                 \\nin \\perp \\prop ...
