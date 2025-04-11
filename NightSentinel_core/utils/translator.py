import re
from cssselect import HTMLTranslator as OriginalHTMLTranslator
from cssselect.parser import Element, FunctionalPseudoElement, PseudoElement
from cssselect.xpath import ExpressionError
from cssselect.xpath import XPathExpr as OriginalXPathExpr
from w3lib.html import HTML5_WHITESPACE
from typing import Optional

class XPathExpr(OriginalXPathExpr):
    textnode: bool = False
    attribute: Optional[str] = None

    @classmethod
    def from_xpath(cls, xpath: OriginalXPathExpr, textnode: bool = False, attribute: Optional[str] = None):
        x = cls(path=xpath.path, element=xpath.element, condition=xpath.condition)
        x.textnode = textnode
        x.attribute = attribute
        return x

    def __str__(self):
        path = super().__str__()
        if self.textnode:
            path += "/text()"
        if self.attribute is not None:
            path += f"/@{self.attribute}"
        return path

class HTMLTranslator(OriginalHTMLTranslator):
    def xpath_element(self, selector: Element):
        xpath = super().xpath_element(selector)
        return XPathExpr.from_xpath(xpath)

    def xpath_pseudo_element(self, xpath: OriginalXPathExpr, pseudo_element: PseudoElement):
        if isinstance(pseudo_element, FunctionalPseudoElement):
            if pseudo_element.name == "attr":
                return XPathExpr.from_xpath(xpath, attribute=pseudo_element.arguments[0].value)
        elif pseudo_element.name == "text":
            return XPathExpr.from_xpath(xpath, textnode=True)
        raise ExpressionError(f"Unknown pseudo-element: {pseudo_element.name}")

translator_instance = HTMLTranslator()