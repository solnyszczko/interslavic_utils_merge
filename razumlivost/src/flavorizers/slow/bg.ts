import multireplacer from '../../dsl/multireplacer';

export default () =>
  multireplacer
    .named('Interslavic → Bulgarian')
    .rule('Ignore case', (r) => r.lowerCase())
    .rule('Cyrl', (r) =>
      r.map({
        '’': '',
        a: 'а',
        b: 'б',
        c: 'ц',
        d: 'д',
        e: 'е',
        f: 'ф',
        g: 'г',
        h: 'х',
        i: 'и',
        j: 'й',
        ja: 'я',
        ju: 'ю',
        je: 'е',
        jo: 'ьо',
        k: 'к',
        l: 'л',
        lj: 'л',
        m: 'м',
        n: 'н',
        nj: 'н',
        o: 'о',
        p: 'п',
        r: 'р',
        s: 'с',
        t: 'т',
        u: 'у',
        v: 'в',
        y: 'и',
        z: 'з',
        å: 'а',
        è: 'е',
        ò: 'ъ',
        ù: 'в',
        ć: 'щ',
        č: 'ч',
        čt: 'щ',
        šč: 'щ',
        ď: 'd',
        đ: 'жд',
        ė: 'е',
        ę: 'е',
        ě: 'е',
        ı: '',
        ĺj: 'л',
        ľ: 'л',
        ń: 'н',
        ńj: 'н',
        ŕ: 'ър',
        ś: 'с',
        š: 'ш',
        ť: 'т',
        ų: 'ъ',
        ź: 'з',
        ž: 'ж',
        ȯ: 'ъ',
        ḓ: '',
        ṙ: 'ър',
      }),
    )
    .rule('Restore case', (r) => r.restoreCase())
    .build();
