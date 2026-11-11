.. _cookbook:

********
Cookbook
********

In the cookbook, you can find hints and tips for working with PyFVCOM2.

The examples are grouped by the type of workflow they support:

* creating boundary and nesting files;
* creating restart files;
* preparing and analysing tidal inputs; and
* preparing model data and configuring numerical experiments.

Boundary and nesting files
==========================

These examples show how to create FVCOM nesting files from external model
data, and how to apply tidal corrections to nesting forcing.

.. toctree::
    :maxdepth: 1

    predict_tides_and_adjust_nest_forcing
    generate_nest_forcing_file_from_cmems_data
    generate_nest_forcing_file_from_nemo_output

Restart files
=============

These examples demonstrate how to build FVCOM restart files from CMEMS and
NEMO output, including the optional FVCOM-ERSEM workflow.

.. toctree::
    :maxdepth: 1

    generate_fvcom_restart_using_cmems_data
    generate_fvcom_ersem_restart_from_nemo_output

Tidal inputs and analysis
=========================

These examples cover tidal harmonic analysis, interpolation of tidal
constituents, tide-only input files, and comparison of TPXO products.

.. toctree::
    :maxdepth: 1

    create_tide_only_inputs
    interpolate_tpxo_tidal_harmonics
    compare_tpxo_atlas_vs_coarse
    tidal_harmonic_analysis_fvcom
    tidal_harmonic_analysis_tide_gauge

Model data and experiment setup
===============================

These examples cover interpolation of FVCOM data, bathymetry preparation,
and application of a model spin-up ramp.

.. toctree::
    :maxdepth: 1

    interpolate_fvcom_data
    apply_ramp_demonstration
    bathymetry_smoothing
