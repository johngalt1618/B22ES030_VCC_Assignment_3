resource "google_cloudfunctions_function" "scale_vm" {
  name        = "scale-vm"
  runtime     = "python39"
  entry_point = "scale_vm"
  source_archive_bucket = "your-bucket"
  source_archive_object = "scale_vm.zip"
}
