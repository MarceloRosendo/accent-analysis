# accent-analysis
## Step 1: To collect some data for Model training:
`https://github.com/yt-dlp/yt-dlp` 
Use this lib and run the command:
`python yt-dlp --print "%(id)s" "<channel link>" > <output file name>.txt`

## Step 2: To transcript all videos listed in your file output
- Use the script `download_transcriptions.py`
- Example: download_transcriptions('mineiro', ['id1', 'id2', 'id3', ...])

## Step 3: Use the `analysis.ipynb` for model training
