#include <iostream>
#include <filesystem>
#include <string>
#include <cstdlib>  // Untuk getenv

namespace fs = std::filesystem;

void list_cache(const std::string& path) {
    try {
        if (fs::exists(path) && fs::is_directory(path)) {
            std::cout << "Contents of " << path << ":\n";
            for (const auto& entry : fs::directory_iterator(path)) {
                std::cout << entry.path().string() << std::endl;
            }
        } else {
            std::cerr << "Directory does not exist: " << path << std::endl;
        }
    } catch (const fs::filesystem_error& err) {
        std::cerr << "Filesystem error: " << err.what() << std::endl;
    } catch (const std::exception& ex) {
        std::cerr << "Exception: " << ex.what() << std::endl;
    }
}

void delete_cache(const std::string& path) {
    try {
        if (fs::exists(path) && fs::is_directory(path)) {
            for (const auto& entry : fs::directory_iterator(path)) {
                fs::remove_all(entry);
            }
            std::cout << "Cache deleted successfully in " << path << std::endl;
        } else {
            std::cerr << "Directory does not exist: " << path << std::endl;
        }
    } catch (const fs::filesystem_error& err) {
        std::cerr << "Filesystem error: " << err.what() << std::endl;
    } catch (const std::exception& ex) {
        std::cerr << "Exception: " << ex.what() << std::endl;
    }
}

int main() {
    const char* home = getenv("HOME");
    if (home == nullptr) {
        std::cerr << "Unable to get HOME environment variable" << std::endl;
        return 1;
    }

    std::string cache_path = std::string(home) + "/Library/Caches";
    
    std::cout << "Before deletion:\n";
    list_cache(cache_path);

    delete_cache(cache_path);

    std::cout << "\nAfter deletion:\n";
    list_cache(cache_path);

    return 0;
}
