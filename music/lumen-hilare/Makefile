# Directory containing your LilyPond binary
LILYPOND := ../lilypond/bin/lilypond

# Target directory for generated files
BUILD_DIR := build

# Automatically discover all .ly files except templates
SOURCES := $(filter-out %template-pre.ly %template-post.ly, $(wildcard *.ly) $(wildcard */*.ly))

# Generate corresponding PDF and MIDI target paths in the build folder
PDFS  := $(patsubst %.ly, $(BUILD_DIR)/%.pdf, $(SOURCES))
MIDIS := $(patsubst %.ly, $(BUILD_DIR)/%.midi, $(SOURCES))

# Template files that trigger a rebuild for ALL files if modified
TEMPLATES := ../template-pre.ly ../template-post.ly

.PHONY: all clean

all: $(PDFS)

# Pattern rule: Compile .ly file to PDF/MIDI in build/ directory only if changed
$(BUILD_DIR)/%.pdf $(BUILD_DIR)/%.midi: %.ly $(TEMPLATES)
	@mkdir -p $(dir $@)
	$(LILYPOND) --output=$(basename $@) $<

clean:
	rm -rf $(BUILD_DIR)
