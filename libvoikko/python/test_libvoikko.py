# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from libvoikko import Voikko, unicode_str, Dictionary, Token, Sentence

ALBERTIN_FAGOTTI = 'Albert osti fagotin ja töräytti puhkuvan melodian.'

text_type = unicode_str  # `six` nomenclature


@pytest.fixture(scope='module')
def v(request):
    voikko = Voikko('fi')
    request.addfinalizer(lambda: voikko.terminate())
    return voikko


def test_get_version(v):
    version = Voikko.getVersion()
    assert version
    assert isinstance(version, text_type)


def test_get_dicts():
    dicts = list(Voikko.listDicts())
    assert dicts
    assert all(isinstance(d, Dictionary) for d in dicts)
    assert any(d.language == 'fi' for d in dicts)
    # TODO: a better test? Can't know what dictionaries the user has...


def test_list_supported_spelling_languages(v):
    languages = list(Voikko.listSupportedSpellingLanguages())
    assert languages == ['fi']


def test_list_supported_hyphenation_languages(v):
    languages = list(Voikko.listSupportedHyphenationLanguages())
    assert languages == ['fi']


def test_list_supported_grammar_languages(v):
    languages = list(Voikko.listSupportedGrammarCheckingLanguages())
    assert languages == ['fi']


def test_analyze_kissa(v):
    result = v.analyze('kissa')
    assert isinstance(result, list)
    result = result[0]
    assert result['SIJAMUOTO'] == 'nimento'
    assert result['CLASS'] == 'nimisana'
    assert result['STRUCTURE'] == '=ppppp'


def test_spell(v):
    assert v.spell('kissa') == True
    assert v.spell('kpssa') == False


def test_suggest_kisssa(v):
    assert v.suggest('kisssa') == [u'kissa', u'kissaa', u'kisassa', u'kisussa']


def test_hyphenate(v):
    assert v.hyphenate('kissa') == 'kis-sa'
    assert v.hyphenate('Annikki-vaari') == 'An-nik-ki-vaa-ri'


def test_hyphenation_pattern(v):
    assert v.getHyphenationPattern('Annikki-vaari') == '  -  - =   - '


def test_tokens(v):
    # TODO: should this be tested better?
    tokens = v.tokens(ALBERTIN_FAGOTTI)
    assert len(tokens) == 14
    assert all(isinstance(t, Token) for t in tokens)
    assert tokens[0].tokenType == Token.WORD
    assert tokens[0].tokenText == 'Albert'
    assert all(t.tokenType == Token.WHITESPACE for t in tokens if t.tokenText.isspace())
    assert all(t.tokenType == Token.PUNCTUATION for t in tokens if t.tokenText == '.')


def test_sentences(v):
    text = ' '.join([ALBERTIN_FAGOTTI] * 5)
    sentences = v.sentences(text)
    assert len(sentences) == 5
    assert all(isinstance(s, Sentence) for s in sentences)


def test_no_grammar_errors(v):
    assert not v.grammarErrors(ALBERTIN_FAGOTTI, language='fi')


def test_grammar_errors(v):
    pytest.xfail(reason="Broken test?")  # TODO: How can one make `grammarErrors` output something?
    assert v.grammarErrors('Albert osti fagotti ja töräytti puhkuvan melodia.', language='fi')
