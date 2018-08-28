# _*_ coding: utf-8 _*_
from gtts import gTTS

tts = gTTS(text=u'안녕 리원아 나는 지금 식사중이야', lang='ko')
tts.save('playbook.mp3')

hello = gTTS(text=u'여보세요?', lang='ko')
hello.save('hello.mp3')

playbook_08 = gTTS(text=u'핑크퐁, 자고 있단다. 나중에 다시 전화하렴.', lang='ko')
playbook_08.save('playbook_08.mp3')

playbook_11 = gTTS(text=u'핑크퐁, 유치원 갔단다. 나중에 다시 전화하렴.', lang='ko')
playbook_11.save('playbook_11.mp3')

playbook_13 = gTTS(text=u'핑크퐁, 점심 먹고 있단다. 나중에 다시 전화하렴.', lang='ko')
playbook_13.save('playbook_13.mp3')

playbook_17 = gTTS(text=u'핑크퐁, 스투디오에 촬영하러 갔단다. 나중에 다시 전화하렴.', lang='ko')
playbook_17.save('playbook_17.mp3')

playbook_20 = gTTS(text=u'핑크퐁, 저녁 먹고 있단다. 나중에 다시 전화하렴.', lang='ko')
playbook_20.save('playbook_20.mp3')
