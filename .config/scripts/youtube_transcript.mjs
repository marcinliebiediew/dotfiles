import { getSubtitles } from 'youtube-captions-scraper';

getSubtitles({
  videoID: new URL(process.argv[2]).searchParams.get("v"),
  lang: 'en'
}).then(captions => {
  captions.forEach(item => console.log(item.text));
});
