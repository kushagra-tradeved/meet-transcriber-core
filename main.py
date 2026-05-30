import os
import json
import config
import utils
from engine import ProductionTranscriber

def main():
    # 1. Initialize directory verification paths
    utils.ensure_directories()
    
    # 2. Seek target file inside the recordings drop zone
    files = [f for f in os.listdir(config.RECORDINGS_DIR) if utils.validate_audio_file(os.path.join(config.RECORDINGS_DIR, f))]
    
    if not files:
        print(f"⚠️ No matching audio/video files located inside '{config.RECORDINGS_DIR}' folder.")
        print(" Drop a Google Meet recording (.mp4, .webm, or .mp3) in that directory and rerun.")
        return

    # Pick the oldest unparsed meeting file for processing
    target_file_name = files[0]
    full_target_path = os.path.join(config.RECORDINGS_DIR, target_file_name)
    
    # 3. Spin up processing pipeline
    transcriber = ProductionTranscriber()
    transcript_data = transcriber.process_file(full_target_path)
    
    # 4. Generate structured dual export formats
    output_txt_path = full_target_path + "_transcript.txt"
    output_json_path = full_target_path + "_data.json"
    
    # Export 1: Standard human-readable script text
    with open(output_txt_path, "w", encoding="utf-8") as txt_file:
        for item in transcript_data:
            txt_file.write(f"[{item['start']}s - {item['end']}s] {item['text']}\n")
            
    # Export 2: Pure structured JSON schema for subsequent LLM consumption layers
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(transcript_data, json_file, indent=2, ensure_ascii=False)
        
    print(f"\n🎉 Success! Outputs saved safely:\n➡️ {output_txt_path}\n➡️ {output_json_path}")

if __name__ == "__main__":
    main()