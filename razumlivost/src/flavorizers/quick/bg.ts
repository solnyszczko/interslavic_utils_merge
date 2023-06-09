import multireplacer from '../../dsl/multireplacer';

export default () =>
  multireplacer
    .named('Interslavic → Bulgarian')
    .rule('Ignore case', (r) => r.lowerCase())
    .rule('Etymology', (r) =>
      r.map({
        '’': '',
        å: 'а',
        è: 'е',
        ė: 'ò',
        ò: 'ȯ',
        ù: 'v',
        ď: 'd',
        ę: 'е',
        ě: 'е',
        ı: '',
        ĺj: 'l',
        ľ: 'l',
        ń: 'n',
        ńj: 'n',
        ŕ: 'r',
        ś: 's',
        ť: 't',
        ų: 'ȯ',
        ź: 'z',
        ḓ: '',
        ṙ: 'ȯr',
      }),
    )
    .rule('Cyrl', (r) =>
      r.map({
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
        ć: 'щ',
        č: 'ч',
        čt: 'щ',
        šč: 'щ',
        đ: 'жд',
        ė: 'е',
        š: 'ш',
        ž: 'ж',
        ȯ: 'ъ',
      }),
    )
    .rule('Restore case', (r) => r.restoreCase())
    .build();
