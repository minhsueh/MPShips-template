from core.utils import get_mpr
from dash import Output, Input
import plotly.graph_objects as pgo
from dash.exceptions import PreventUpdate

mpr = get_mpr()


def register_callbacks(app):
    @app.callback(
        Output("fig-real-dielec", "figure"),
        Output("fig-imag-dielec", "figure"),
        Input("input-box", "value"),
        Input("enter-btn", "n_clicks"),
        prevent_initial_call=True,
    )
    def update_figure(input_text, n_clicks):
        if not (input_text or n_clicks):
            raise PreventUpdate

        mpr = get_mpr()

        all_mat_list = mpr.materials.summary.search(
            chemsys=input_text, fields=["material_id", "has_props"]
        )

        opt_mpids = []
        for mat in all_mat_list:
            if mat.has_props["absorption"]:
                opt_mpids.append(mat.material_id)

        mat_op_docs = mpr.materials.absorption.search(
            material_ids=opt_mpids,
            fields=[
                "material_id",
                "formula_pretty",
                "energies",
                "average_imaginary_dielectric",
                "average_real_dielectric",
            ],
        )

        fig_real = pgo.Figure()
        fig_imag = pgo.Figure()

        for absorbtion_doc in mat_op_docs:
            fig_real.add_trace(
                pgo.Scatter(
                    x=absorbtion_doc.energies,
                    y=absorbtion_doc.average_real_dielectric,
                    name=absorbtion_doc.formula_pretty,
                    showlegend=True,
                )
            )

            fig_imag.add_trace(
                pgo.Scatter(
                    x=absorbtion_doc.energies,
                    y=absorbtion_doc.average_imaginary_dielectric,
                    name=absorbtion_doc.formula_pretty,
                    showlegend=True,
                )
            )
        fig_real.update_layout(
            title="Real dielectric function",
            title_x=0.5,
            xaxis={
                "title_text": "Energy (eV)",
            },
            yaxis={
                "title_text": "ε<sub>1</sub>",
            },
        )
        fig_imag.update_layout(
            title="Imaginary dielectric function",
            title_x=0.5,
            xaxis={
                "title_text": "Energy (eV)",
            },
            yaxis={
                "title_text": "ε<sub>2</sub>",
            },
        )

        return fig_real, fig_imag
