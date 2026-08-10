assertEqual(a, b): Sprawdza, czy a == b.
assertNotEqual(a, b): Sprawdza, czy a != b.
assertTrue(x): Sprawdza, czy x jest prawdziwe (truthy).
assertFalse(x): Sprawdza, czy x jest fałszywe (falsy).
assertIs(a, b): Sprawdza, czy a is b (czy obiekty to te same instancje).
assertIsNot(a, b): Sprawdza, czy a is not b.
assertIsNone(x): Sprawdza, czy x is None.
assertIsNotNone(x): Sprawdza, czy x is not None.
assertIn(a, b): Sprawdza, czy a in b.
assertNotIn(a, b): Sprawdza, czy a not in b.
assertRaises(Exception, callable, *args, **kwargs): Sprawdza, czy podczas
wykonywania callable zostanie rzucony oczekiwany wyjątek.