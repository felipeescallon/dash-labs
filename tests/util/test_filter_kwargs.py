import dash_express as dx
from dash.development.base_component import Component


def test_filter_nones_and_undefined():
    result = dx.util.filter_kwargs(
        a=12,
        b="Foo",
        c=None,
        d=["A", "B"],
        e=Component.UNDEFINED,
        f={"a": 1, "b": 2},
        g=None,
    )
    assert result == dict(a=12, b="Foo", d=["A", "B"], f={"a": 1, "b": 2})