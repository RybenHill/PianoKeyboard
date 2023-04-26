import pygame
import soundfile as sf

# FIXME - Not working ('soundfile' lib bug?).
# Only MIDI so far.
def convert_aiff_to_wav(aiff_file_path):
    """
    Convert .aiff file to .wav format.

    Args:
        aiff_file_path (str): Path to the .aiff file.

    Returns:
        str: Path to the converted .wav file.
    """
    try:
        # Read the .aiff file
        open(aiff_file_path, 'r')  
        data, sample_rate = sf.read(aiff_file_path)

        # Construct the .wav file name by replacing the extension
        wav_file_path = aiff_file_path.replace('.aiff', '.wav')

        # Create the .wav file with the given file name
        open(wav_file_path, 'w')  

        # Write the data to .wav format
        sf.write(wav_file_path, data, sample_rate)

        print(f"Successfully converted {aiff_file_path} to {wav_file_path}")
        return wav_file_path
    
    except Exception as e:
        print(f"Failed to convert {aiff_file_path} to .wav format: {e}")
        return None

# TODO - Support multiple octaves
# TODO - Support multiple scales
# TODO - Customizable mapping
def mapMIDI2Keyboard(midi_notes):
    midi_notes = {
        pygame.K_a: 60,  # Nota C
        pygame.K_s: 62,  # Nota D
        pygame.K_d: 64,  # Nota E
        pygame.K_f: 65,  # Nota F
        pygame.K_g: 67,  # Nota G
        pygame.K_h: 69,  # Nota A
        pygame.K_j: 71,  # Nota B
    }
    return midi_notes
