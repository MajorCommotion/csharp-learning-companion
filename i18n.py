#!/usr/bin/env python3
"""
i18n (Internationalization) module for C# / ASP.NET Learning Companion
Supports multiple languages with JSON-based translation files.
"""

import json
import os
from typing import Dict, Any, Optional


class I18n:
    """Internationalization handler."""
    
    SUPPORTED_LANGUAGES = {
        'en': 'English',
        'ko': '한국어 (Korean)'
    }
    
    def __init__(self, default_language: str = 'en'):
        """Initialize i18n with default language."""
        self.current_language = default_language
        self.translations: Dict[str, Dict] = {}
        self._load_all_translations()
    
    def _load_all_translations(self):
        """Load all available translation files."""
        locales_dir = os.path.join(os.path.dirname(__file__), 'locales')
        
        if not os.path.exists(locales_dir):
            raise FileNotFoundError(f"Locales directory not found: {locales_dir}")
        
        for lang_code in self.SUPPORTED_LANGUAGES.keys():
            filepath = os.path.join(locales_dir, f'{lang_code}.json')
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.translations[lang_code] = json.load(f)
            else:
                print(f"Warning: Translation file not found: {filepath}")
    
    def set_language(self, lang_code: str) -> bool:
        """Set current language."""
        if lang_code in self.SUPPORTED_LANGUAGES:
            self.current_language = lang_code
            return True
        return False
    
    def get_language_name(self, lang_code: Optional[str] = None) -> str:
        """Get language name."""
        code = lang_code or self.current_language
        return self.SUPPORTED_LANGUAGES.get(code, 'Unknown')
    
    def t(self, key: str, **kwargs) -> str:
        """
        Translate a key to current language.
        
        Args:
            key: Translation key (supports dot notation: "menu.exit")
            **kwargs: Optional format arguments
        
        Returns:
            Translated string
        """
        # Get translation for current language
        translation = self._get_nested_value(
            self.translations.get(self.current_language, {}),
            key
        )
        
        # Fallback to English if not found
        if translation is None:
            translation = self._get_nested_value(
                self.translations.get('en', {}),
                key
            )
        
        # Fallback to key itself if still not found
        if translation is None:
            return key
        
        # Format if kwargs provided
        if kwargs:
            try:
                return translation.format(**kwargs)
            except KeyError:
                return translation
        
        return translation
    
    def _get_nested_value(self, data: Dict, key: str) -> Optional[str]:
        """Get value from nested dictionary using dot notation."""
        keys = key.split('.')
        value = data
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return None
        
        return value if isinstance(value, str) else None
    
    def list_languages(self) -> Dict[str, str]:
        """List all supported languages."""
        return self.SUPPORTED_LANGUAGES.copy()


# Global i18n instance
_i18n = I18n()


def get_i18n() -> I18n:
    """Get global i18n instance."""
    return _i18n


def t(key: str, **kwargs) -> str:
    """Shorthand for translation."""
    return _i18n.t(key, **kwargs)
