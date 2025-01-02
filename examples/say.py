"""Use macOS native speech synthesis from Python"""

import sys

import AVFoundation
from Foundation import NSObject
from PyObjCTools.AppHelper import runEventLoop, stopEventLoop


class SpeechSynthesizerDelegate(NSObject):
    def speechSynthesizer_didFinishSpeechUtterance_(self, synthesizer, utterance):
        stopEventLoop()


def speak_string(text: str) -> None:
    synthesizer = AVFoundation.AVSpeechSynthesizer.alloc().init()
    utterance = AVFoundation.AVSpeechUtterance.speechUtteranceWithString_(text)
    voice = AVFoundation.AVSpeechSynthesisVoice.voiceWithLanguage_("en-US")
    utterance.setVoice_(voice)
    utterance.setRate_(AVFoundation.AVSpeechUtteranceDefaultSpeechRate)
    delegate = SpeechSynthesizerDelegate.alloc().init()
    synthesizer.setDelegate_(delegate)
    synthesizer.speakUtterance_(utterance)
    runEventLoop()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing string, nothing to say.", file=sys.stderr)
        sys.exit(1)
    speak_string(sys.argv[1])
