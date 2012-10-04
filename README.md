Asciimath
=========

Converts ascii math to utf8
##Examples
        asciimath '\int f_1(x)f_2(x)d\mu') ->  '∫ f₁(x)f₂(x)dμ'
        asciimath 'cos(\pi) = -1'          ->  'cos(π) = -1'
        asciimath 'a^\\alpha = \\tau'      ->  'aᵅ = τ'

##UTF8-limitations
        very few greek symbols are possible to sup and subscript
            supscriptable:  α β γ δ ε θ ι Φ φ χ
            subscriptable:  β ι ρ φ χ

        Capital letters are not possible to subscript at all
        Supscriptable capitals: A B D E G H I J K L M N O P R T U V W


##Symbols
        greek letters:       \\alpha  etc
        superscript letter:  ^
        subscript letter:    _
        math symbols:        \\int \\sum \\prod \\in \\exist \\forall
                                 \\nin \\perp \\prop ...
